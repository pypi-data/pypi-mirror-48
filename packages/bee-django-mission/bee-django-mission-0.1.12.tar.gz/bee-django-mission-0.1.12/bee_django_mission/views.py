# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json, qrcode, os, shutil, urllib
from django.shortcuts import get_object_or_404, reverse, redirect, render
from django.views.generic import ListView, DetailView, TemplateView, RedirectView
from django.db.models import Q, Sum, Count
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.utils.datastructures import MultiValueDict
from django.contrib import messages
from django.http import HttpResponse
from django.conf import settings
from django.utils.six import BytesIO
from django.apps import apps
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from django import forms
from django.contrib.auth.decorators import permission_required
from django.db import transaction
from django.db.models import Case, When, Value, CharField

from .decorators import cls_decorator, func_decorator
from .models import Line, Stage, Mission, UserLine, UserStage, UserMission, UserStageFinishCount, CustomUserMission
from .utils import check_add_user_line, get_current_week_stage, get_top_prize
from .forms import MissionForm, StageUnlimitedForm, UserLineCreateForm, UserMissionForm
from .http import JSONResponse
from .dt import get_now


# from .forms import UserStageFinishForm
User = get_user_model()


# Create your views here.
def test(request):
    user = request.user
    stage = Stage.objects.all().first()
    _sum = 0
    for i in range(1, 1000):
        coin = stage.get_prize_coin()
        _sum += coin
        print(coin)
    print('===sum===' + _sum.__str__())
    # ====init
    # line = Line.objects.all().filter(line_type=2).first()
    # u_l = UserLine()
    # u_l.line = line
    # u_l.user = user
    # u_l.save()

    # ====check mission
    # ret=check_user_mission_finish(user)
    # ul=UserLine.objects.all().first()
    # us.finish_and_start_next_user_stage()


    # print(ret)
    # ==update missions
    # user_stage = UserStage.objects.get(id=1)
    # user_stage.add_user_missions()
    return HttpResponse("Ok")


def test_fix_user_stage_token(request):
    import random, string
    user_stage_list = UserStage.objects.all().values('name', "stage_id", "user_line__line_id").order_by(
        'name').distinct()
    for user_stage in user_stage_list:
        r = ''.join(random.sample(string.ascii_letters + string.digits, 10))

        line_id = user_stage["user_line__line_id"]
        stage_id = user_stage["stage_id"]
        name = user_stage["name"]
        _user_stage_list = UserStage.objects.filter(user_line__line__id=line_id, stage__id=stage_id, name=name)
        for i in _user_stage_list:
            i.token = r
            i.save()
    return HttpResponse("Ok")


# ======Stage start =========
class StageList(ListView):
    model = Stage
    template_name = 'bee_django_mission/stage/list.html'
    context_object_name = 'stage_list'
    paginate_by = 20


class StageUnlimitedList(StageList):
    template_name = 'bee_django_mission/stage/unlimited_list.html'
    line_type = 1

    def get_queryset(self):
        queryset = super(StageUnlimitedList, self).get_queryset()
        return queryset.filter(line__line_type=self.line_type)

    def get_context_data(self, **kwargs):
        context = super(StageUnlimitedList, self).get_context_data(**kwargs)
        line = Line.objects.get(line_type=self.line_type)
        context["line"] = line
        return context


# class StageDetail(DetailView):
#     model = Mission
#     template_name = 'bee_django_mission/mission/detail.html'
#     context_object_name = 'mission'


@method_decorator(cls_decorator(cls_name='StageCreate'), name='dispatch')
class StageCreate(CreateView):
    model = Stage
    form_class = StageUnlimitedForm
    template_name = 'bee_django_mission/stage/form.html'

    # def get_context_data(self, **kwargs):
    #     context = super(StageCreate, self).get_context_data(**kwargs)
    #     line = Line.objects.get(id=self.kwargs["line_id"])
    #     context["line"] = line
    #     return context
    #
    # def form_valid(self, form):
    #     stage = form.save(commit=False)
    #     line = Line.objects.get(id=self.kwargs["line_id"])
    #     stage.line = line
    #     stage.save()
    #     return super(StageCreate, self).form_valid(form)


@method_decorator(cls_decorator(cls_name='StageUpdate'), name='dispatch')
class StageUpdate(UpdateView):
    model = Stage
    form_class = StageUnlimitedForm
    template_name = 'bee_django_mission/stage/form.html'
    #
    # def get_context_data(self, **kwargs):
    #     context = super(StageUpdate, self).get_context_data(**kwargs)
    #     line = Line.objects.get(stage__id=self.kwargs["pk"])
    #     context["line"] = line
    #     return context


@method_decorator(cls_decorator(cls_name='StageDelete'), name='dispatch')
class StageDelete(DeleteView):
    model = Mission
    success_url = reverse_lazy('bee_django_mission:stage_list')

    def get(self, request, *args, **kwargs):
        return self.http_method_not_allowed(request, *args, **kwargs)


# ======Mission end =========


# ======Mission start =========
class MissionList(ListView):
    model = Mission
    template_name = 'bee_django_mission/mission/list.html'
    context_object_name = 'mission_list'
    paginate_by = 20

    # def get_context_data(self, **kwargs):
    #     context = super(MissionList, self).get_context_data(**kwargs)
    #
    #     return context


class MissionDetail(DetailView):
    model = Mission
    template_name = 'bee_django_mission/mission/detail.html'
    context_object_name = 'mission'


@method_decorator(permission_required('bee_django_mission.add_mission'), name='dispatch')
class MissionCreate(CreateView):
    model = Mission
    form_class = None
    template_name = 'bee_django_mission/mission/form.html'
    fields = ['mission_type', "stage", "name", "count", "info", 'order_by']

    def get_context_data(self, **kwargs):
        context = super(MissionCreate, self).get_context_data(**kwargs)
        line = Line.objects.get(line_type=self.kwargs["line_type"])
        context["line"] = line
        context["form"] = MissionForm(instance=self.object, line=line)
        return context


@method_decorator(permission_required('bee_django_mission.change_mission'), name='dispatch')
class MissionUpdate(UpdateView):
    model = Mission
    form_class = None
    template_name = 'bee_django_mission/mission/form.html'

    fields = ['mission_type', "stage", "name", "count", "info", 'order_by']

    def get_context_data(self, **kwargs):
        context = super(MissionUpdate, self).get_context_data(**kwargs)
        line = Line.objects.get(line_type=self.kwargs["line_type"])
        context["line"] = line
        context["form"] = MissionForm(instance=self.object, line=line)
        return context

        # def get_context_data(self, **kwargs):
        #     context = super(MissionUpdate, self).get_context_data(**kwargs)
        #     # context["source"] = Source.objects.get(id=self.kwargs["pk"])
        #     return context


@method_decorator(permission_required('bee_django_mission.delete_mission'), name='dispatch')
class MissionDelete(DeleteView):
    model = Mission
    success_url = reverse_lazy('bee_django_mission:mission_list')

    def get(self, request, *args, **kwargs):
        return self.http_method_not_allowed(request, *args, **kwargs)


# 周任务
class UserMissionListWeek(TemplateView):
    line_type = 2
    template_name = 'bee_django_mission/user/mission/week_list.html'

    def get_context_data(self, **kwargs):
        context = super(UserMissionListWeek, self).get_context_data(**kwargs)
        user_id = self.kwargs["user_id"]
        user = get_object_or_404(User, pk=user_id)
        context["user"] = user
        try:
            user_line = UserLine.objects.get(user=user, line__line_type=self.line_type)
        except:
            user_line, msg = check_add_user_line(user, 2, check=False)
            if not user_line:
                messages.error(self.request, msg)
                return context


        # # 获取[进行中/已完成/未完成/可完成但未完成]的user_stage
        # user_stage = get_current_week_stage(user)
        # # 没有本周任务，则新增加一个
        # if not user_stage:
        #     user_stage = user_line.check_add_user_stage(check=False)
        new_user_stage = user_line.check_add_user_stage()
        if new_user_stage:
            user_stage = new_user_stage
        else:
            user_stage = get_current_week_stage(user)
        if not user_stage:
            messages.error(self.request, "还没有周任务")
            return context

        # 更新mission状态
        user_stage.update_user_mission()
        # 更新阶段任务的完成状态
        user_stage.update_user_stage_status()
        # 取值
        user_stage_list = user_line.get_user_all_stage()
        user_mission_list = UserMission.objects.filter(user_stage=user_stage).order_by('mission__order_by')
        context["user_stage"] = user_stage
        context["user_stage_list"] = user_stage_list
        context["user_mission_list"] = user_mission_list
        finish_rank_list = UserStageFinishCount.objects.filter(line=user_stage.user_line.line).filter(
            finish_count__gt=0).order_by("-finish_count")[:10]
        context["finish_rank_list"] = finish_rank_list
        context["max_prize_coin"] = user_stage.stage.get_max_prize_coin()
        context["prize_coin_list"] = user_stage.stage.stageprize_set.order_by("-coin")
        context["top_prize_list"] = get_top_prize()
        return context


class CustomUserMissionListWeek(UserMissionListWeek):
    template_name = 'bee_django_mission/user/mission/custom_user_week_list.html'


# 长期任务
class UserMissionListUnlimited(TemplateView):
    line_type = 1
    template_name = 'bee_django_mission/user/mission/unlimited_list.html'

    def get_context_data(self, **kwargs):
        context = super(UserMissionListUnlimited, self).get_context_data(**kwargs)
        user_id = self.kwargs["user_id"]
        user = get_object_or_404(User, pk=user_id)
        context["user"] = user
        try:
            user_line = UserLine.objects.get(user=user, line__line_type=self.line_type)
        except:
            context["add_user_line"] = True
            messages.error(self.request, "还没有任务线")
            return context

        # 获取[进行中/已完成/未完成/可完成但未完成]的user_stage
        user_stage = user_line.get_last_user_stage()

        if not user_stage:
            messages.error(self.request, "还没有阶段任务")
            return context

        # 更新mission状态
        user_stage.update_user_mission()
        # 更新阶段任务的完成状态
        user_stage.update_user_stage_status()
        # 取值
        user_stage_list = user_line.get_user_all_stage()
        user_mission_list = UserMission.objects.filter(user_stage=user_stage)
        context["user"] = user
        context["user_stage"] = user_stage
        context["user_stage_list"] = user_stage_list
        # context["user_mission_list"] = user_mission_list
        return context


class CustomUserMissionListUnlimited(UserMissionListUnlimited):
    template_name = 'bee_django_mission/user/mission/custom_user_unlimited_list.html'


class UserLineCreate(CreateView):
    model = UserLine
    form_class = UserLineCreateForm
    template_name = 'bee_django_mission/user/line/form.html'
    success_url = None

    def get_context_data(self, **kwargs):
        context = super(UserLineCreate, self).get_context_data(**kwargs)
        user_id = self.kwargs["user_id"]
        user = get_object_or_404(User, pk=user_id)
        context['user'] = user
        return context

    # def post(self, request, *args, **kwargs):
    def form_valid(self, form):
        user_line = form.save(commit=False)
        line = user_line.line
        user_id = self.kwargs["user_id"]
        user = get_object_or_404(User, pk=user_id)
        user_line.user = user
        user_line.save()
        self.success_url = reverse('bee_django_mission:user_line_unlimited', kwargs=self.kwargs)
        return super(UserLineCreate, self).form_valid(form)


# 根据line列出所有user_stage
class UserStageList(ListView):
    model = UserStage
    template_name = 'bee_django_mission/stage/user_stage_list.html'
    context_object_name = 'user_stage_list'
    paginate_by = 20
    queryset = None

    def get_queryset(self):
        queryset = UserStage.objects.all().values('name', "user_line__line__name", 'token').order_by('name').distinct()
        return queryset


class UserStageReport(TemplateView):
    template_name = 'bee_django_mission/stage/user_stage_report.html'

    def get_context_data(self, **kwargs):
        context = super(UserStageReport, self).get_context_data(**kwargs)
        user_stage_list = UserStage.objects.filter(token=self.kwargs["token"])
        user_stage = user_stage_list.first()
        # 人数统计
        status_tuple = ((0, '打开过任务页，但未完成'), (1, '已完成'), (2, '未完成'), (3, '可完成但未完成'))
        status_case_list = [When(stutas=item[0], then=Value(item[1])) for i, item in enumerate(status_tuple)]
        status_list = UserStage.objects.filter(token=self.kwargs["token"]).values("stutas") \
            .annotate(c=Count("id")) \
            .annotate(name=Case(*status_case_list, default=Value('无'), output_field=CharField())) \
            .order_by("stutas")
        # m币奖励统计

        prize_list = UserStage.objects.filter(token=self.kwargs["token"], stutas=1).values("prize_coin") \
            .annotate(c=Count("id")) \
            .order_by("-prize_coin")
        context["status_list"] = status_list
        context["user_stage"] = user_stage
        context["prize_list"] = prize_list

        return context

    def get(self, request, *args, **kwargs):
        return super(UserStageReport, self).get(request, *args, **kwargs)

        # def get_context_data(self, **kwargs):
        #     context = super(MissionList, self).get_context_data(**kwargs)
        #
        #     return context


@method_decorator(cls_decorator(cls_name='UserStageDetail'), name='dispatch')
class UserStageDetail(DetailView):
    model = UserStage
    template_name = 'bee_django_mission/user/mission/unlimited_list.html'
    context_object_name = 'user_stage'

    def get_context_data(self, **kwargs):
        context = super(UserStageDetail, self).get_context_data(**kwargs)
        user_stage = get_object_or_404(UserStage, pk=self.kwargs["pk"])
        # 更新mission状态
        user_stage.update_user_mission()
        # 更新阶段任务的完成状态
        user_stage.update_user_stage_status()
        # 取值
        user_stage_list = user_stage.user_line.get_user_all_stage()
        user_mission_list = UserMission.objects.filter(user_stage=user_stage)
        context["user"] = user_stage.user_line.user
        context["user_stage"] = user_stage
        context["user_stage_list"] = user_stage_list
        context["user_mission_list"] = user_mission_list
        return context


class CustomUserStageDetail(UserStageDetail):
    template_name = ''


class UserStageUpdateStatus(TemplateView):
    def post(self, request, *args, **kwargs):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        try:
            user_stage_id = self.kwargs['user_stage_id']
            status = self.kwargs['status']
            user_stage = get_object_or_404(UserStage, pk=user_stage_id)
            # 完成任务，并发奖励
            res = user_stage.finish_user_stage_add_prize()
            # 检查添加下一阶段任务
            user_stage.user_line.check_add_user_stage()
            msg = ''
            if res:
                msg = '操作成功'
            if not res:
                msg = '此任务已完成'
            res = {"error": 0, "msg": msg}
        except Exception as e:
            print(e)
            res = {"error": 1, "msg": "操作失败"}

        return JSONResponse(json.dumps(res, ensure_ascii=False))


@method_decorator(permission_required('bee_django_mission.can_reset_user_mission'), name='dispatch')
class UserStageUpdateMission(TemplateView):
    def post(self, request, *args, **kwargs):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        try:
            user_stage_id = self.kwargs['user_stage_id']
            user_stage = get_object_or_404(UserStage, pk=user_stage_id)
            user_stage.update()
            res = {"error": 0, "msg": "操作成功"}
        except Exception as e:
            print(e)
            res = {"error": 1, "msg": "操作失败"}

        return JSONResponse(json.dumps(res, ensure_ascii=False))


class UserStageUpdate(UpdateView):
    model = UserMission
    form_class = UserMissionForm
    template_name = 'bee_django_mission/user/mission/form.html'

    def get_success_url(self):
        user_mission = get_object_or_404(UserMission, id=self.kwargs["pk"])
        user = user_mission.user_stage.user_line.user
        line = user_mission.user_stage.user_line.line
        if line.is_week_line():
            return reverse('bee_django_mission:user_line_week', kwargs={"user_id": user.id})
        if line.is_unlimited_line():
            return reverse('bee_django_mission:user_unlimited_week', kwargs={"user_id": user.id})

    @transaction.atomic
    def form_valid(self, form):
        if not self.request.user.has_perm('bee_django_mission.add_customusermission'):
            messages.error(self.request, '没有权限')
            return redirect(reverse('bee_django_mission:user_stage_update', kwargs=self.kwargs))

        if form.is_valid():
            # 新建或修改规则模版
            user_mission = form.save(commit=True)
            user = user_mission.user_stage.user_line.user
            stage = user_mission.user_stage.stage
            try:
                custom_mission = CustomUserMission.objects.get(user=user, stage=stage,
                                                               mission=user_mission.mission)
            except:
                custom_mission = CustomUserMission()
                custom_mission.user = user
                custom_mission.stage = stage
                custom_mission.mission = user_mission.mission
            custom_mission.custom_name = user_mission.custom_name
            custom_mission.custom_count = user_mission.custom_count
            custom_mission.save()
            messages.success(self.request, '修改成功')
        return super(UserStageUpdate, self).form_valid(form)


class UserStageFinishRankList(TemplateView):
    template_name = 'bee_django_mission/user/stage/finish/rank_list.html'

    def get_context_data(self, **kwargs):
        context = super(UserStageFinishRankList, self).get_context_data(**kwargs)
        line = get_object_or_404(Line, pk=self.kwargs["line_id"])
        finish_rank_list = UserStageFinishCount.objects.filter(line=line).filter(
            finish_count__gt=0).order_by("-finish_count")
        context["line"] = line
        context["finish_rank_list"] = finish_rank_list
        return context


class CustomUserStageFinishRankList(UserStageFinishRankList):
    template_name = 'bee_django_mission/user/stage/finish/custom_rank_list.html'

# from django.http import HttpResponse
from typing import AbstractSet
from django.forms import widgets
from django.shortcuts import render, redirect
from statics.forms import UserCreationForm, EditProfileForm
# from tutorial__.forms import UserCreationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse

from django.shortcuts import render, redirect

from statics.forms import Static8FForm, Static6FForm
# from tutorial__.forms import Static8FForm, Static6FForm
from statics.models import Static8FModel, Static6FModel

from anastruct import SystemElements


from django.views.generic import TemplateView

import time



# @login_required
# def home(request):
#     # return HttpResponse("Home Page!")
#     number = [1, 2, 3, 4, "bla", 34]
#     name = 'test'
#     args = {'myname': name, 'numbers': number}
#     return render(request, 'statics/home.html', args)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/statics')
    else:
        form = UserCreationForm()

        args = {'form': form}
        return render(request, 'statics/reg_form.html', args)


@login_required
def view_profile(request):
    args = {'user': request.user}
    # print(reverse('view_profile').lstrip('/'))
    # return render(request, reverse('view_profile').lstrip('/'), args)

    return render(request, 'statics/profile.html', args)
    # return render(request, '/statics/profile', args)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('view_profile'))
            # return redirect('/statics/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'statics/edit_profile.html', args)







class Static8FView(TemplateView):

    template_name = 'statics/static8F.html'

    @method_decorator(login_required)
    def get(self, request):
        obj = Static8FModel.objects.last()
        if obj == None:
            LGesamt = ""
            LSammler = ""
            Fabstand1 = ""
            Fabstand2 = ""
            Fabstand3 = ""
            mLeer = ""
            mSammler = ""
            VRohr = ""

            F12Leer = 0.0
            F34Leer = 0.0
            F56Leer = 0.0
            F78Leer = 0.0

            F12Voll = 0.0
            F34Voll = 0.0
            F56Voll = 0.0
            F78Voll = 0.0
        else:
            LGesamt = getattr(obj, 'LGesamt')
            LSammler = getattr(obj, 'LSammler')
            Fabstand1 = getattr(obj, 'Fabstand1')
            Fabstand2 = getattr(obj, 'Fabstand2')
            Fabstand3 = getattr(obj, 'Fabstand3')
            mLeer = getattr(obj, 'mLeer')
            mSammler = getattr(obj, 'mSammler')
            VRohr = getattr(obj, 'VRohr')

            F12Leer = getattr(obj, 'F12Leer')
            F34Leer = getattr(obj, 'F34Leer')
            F56Leer = getattr(obj, 'F56Leer')
            F78Leer = getattr(obj, 'F78Leer')

            F12Voll = getattr(obj, 'F12Voll')
            F34Voll = getattr(obj, 'F34Voll')
            F56Voll = getattr(obj, 'F56Voll')
            F78Voll = getattr(obj, 'F78Voll')

        initial = {'LGesamt': LGesamt, 'LSammler': LSammler, 'Fabstand1': Fabstand1, 'Fabstand2': Fabstand2,
                   'Fabstand3': Fabstand3, 'mLeer': mLeer, 'mSammler': mSammler, 'VRohr': VRohr}

        form = Static8FForm(initial)

        args = {'form': form, 'F12Leer': F12Leer, 'F34Leer': F34Leer, 'F56Leer': F56Leer, 'F78Leer': F78Leer,
                'F12Voll': F12Voll, 'F34Voll': F34Voll, 'F56Voll': F56Voll, 'F78Voll': F78Voll}

        return render(request, self.template_name, args)

    @method_decorator(login_required)
    def post(self, request):
        form = Static8FForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user

            LGesamt = post.LGesamt
            LSammler = post.LSammler
            Fabstand1 = post.Fabstand1
            Fabstand2 = post.Fabstand2
            Fabstand3 = post.Fabstand3
            mLeer = post.mLeer
            mSammler = post.mSammler
            VRohr = post.VRohr

            proof = 1

            if LGesamt <= 0 or LSammler <= 0:
                proof = 0
            if Fabstand1 <= 0 or Fabstand2 <= 0 or Fabstand3 <= 0:
                proof = 0
            if LSammler >= LGesamt or Fabstand1 >= LGesamt or Fabstand2 >= LGesamt or Fabstand3 >= LGesamt:
                proof = 0
            if mLeer <= 0 or mSammler <= 0 or VRohr <= 0:
                proof = 0
            if mLeer <= mSammler:
                proof = 0

            if proof == 1:
                LGesamt_m   = LGesamt/1000
                LSammler_m  = LSammler/1000
                Fabstand1_m = Fabstand1/1000
                Fabstand2_m = Fabstand2/1000
                Fabstand3_m = Fabstand3/1000
                mLeer_oS    = mLeer - mSammler
                mVoll_oS    = mLeer_oS + VRohr

                forceSammler = mSammler * 9.81
                forceLeer_oS = mLeer_oS * 9.81
                forceVoll_oS = mVoll_oS * 9.81

                loadLeer_oS = forceLeer_oS/LGesamt_m
                loadVoll_oS = forceVoll_oS/LGesamt_m

                ss = SystemElements(EA=25000, EI=5000)

                ss.add_element(location=[[0, 0], [LSammler_m, 0]])
                ss.add_element(location=[[LSammler_m, 0], [
                               (Fabstand1_m+LSammler_m), 0]])
                ss.add_element(location=[
                               [(Fabstand1_m+LSammler_m), 0], [(Fabstand2_m+Fabstand1_m+LSammler_m), 0]])
                ss.add_element(location=[[(Fabstand2_m+Fabstand1_m+LSammler_m), 0], [
                               (Fabstand3_m+Fabstand2_m+Fabstand1_m+LSammler_m), 0]])

                ss.add_support_hinged(node_id=[2, 3, 4, 5])

                ss.point_load(Fy=-forceSammler, node_id=1)
                ss.q_load(q=-loadLeer_oS, element_id=2)
                ss.q_load(q=-loadLeer_oS, element_id=3)
                ss.q_load(q=-loadLeer_oS, element_id=4)

                ss.solve()

                post.F12Leer = abs(
                    round(ss.reaction_forces[2].Fz/100, 0)*100)/2
                post.F34Leer = abs(
                    round(ss.reaction_forces[3].Fz/100, 0)*100)/2
                post.F56Leer = abs(
                    round(ss.reaction_forces[4].Fz/100, 0)*100)/2
                post.F78Leer = abs(
                    round(ss.reaction_forces[5].Fz/100, 0)*100)/2

                ss.q_load(q=-loadVoll_oS, element_id=2)
                ss.q_load(q=-loadVoll_oS, element_id=3)
                ss.q_load(q=-loadVoll_oS, element_id=4)

                ss.solve()

                post.F12Voll = abs(
                    round(ss.reaction_forces[2].Fz/100, 0)*100)/2
                post.F34Voll = abs(
                    round(ss.reaction_forces[3].Fz/100, 0)*100)/2
                post.F56Voll = abs(
                    round(ss.reaction_forces[4].Fz/100, 0)*100)/2
                post.F78Voll = abs(
                    round(ss.reaction_forces[5].Fz/100, 0)*100)/2

            post.save()
            return redirect('statics:static8F')

        args = {'form': form}
        return render(request, self.template_name, args)


class Static6FView(TemplateView):

    template_name = 'statics/static6F.html'

    @method_decorator(login_required)
    def get(self, request):
        obj = Static6FModel.objects.last()
        if obj == None:
            LGesamt = ""
            LSammler = ""
            Fabstand1 = ""
            Fabstand2 = ""
            mLeer = ""
            mSammler = ""
            VRohr = ""

            F12Leer = 0.0
            F34Leer = 0.0
            F56Leer = 0.0

            F12Voll = 0.0
            F34Voll = 0.0
            F56Voll = 0.0
        else:
            LGesamt = getattr(obj, 'LGesamt')
            LSammler = getattr(obj, 'LSammler')
            Fabstand1 = getattr(obj, 'Fabstand1')
            Fabstand2 = getattr(obj, 'Fabstand2')
            mLeer = getattr(obj, 'mLeer')
            mSammler = getattr(obj, 'mSammler')
            VRohr = getattr(obj, 'VRohr')

            F12Leer = getattr(obj, 'F12Leer')
            F34Leer = getattr(obj, 'F34Leer')
            F56Leer = getattr(obj, 'F56Leer')

            F12Voll = getattr(obj, 'F12Voll')
            F34Voll = getattr(obj, 'F34Voll')
            F56Voll = getattr(obj, 'F56Voll')

        initial = {'LGesamt': LGesamt, 'LSammler': LSammler, 'Fabstand1': Fabstand1, 'Fabstand2': Fabstand2,
                   'mLeer': mLeer, 'mSammler': mSammler, 'VRohr': VRohr}

        form = Static6FForm(initial)

        args = {'form': form, 'F12Leer': F12Leer, 'F34Leer': F34Leer, 'F56Leer': F56Leer,
                'F12Voll': F12Voll, 'F34Voll': F34Voll, 'F56Voll': F56Voll}

        return render(request, self.template_name, args)

    @method_decorator(login_required)
    def post(self, request):
        form = Static6FForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user

            LGesamt = post.LGesamt
            LSammler = post.LSammler
            Fabstand1 = post.Fabstand1
            Fabstand2 = post.Fabstand2
            mLeer = post.mLeer
            mSammler = post.mSammler
            VRohr = post.VRohr

            proof = 1

            if LGesamt <= 0 or LSammler <= 0:
                proof = 0
            if Fabstand1 <= 0 or Fabstand2 <= 0:
                proof = 0
            if LSammler >= LGesamt or Fabstand1 >= LGesamt or Fabstand2 >= LGesamt:
                proof = 0
            if mLeer <= 0 or mSammler <= 0 or VRohr <= 0:
                proof = 0
            if mLeer <= mSammler:
                proof = 0

            if proof == 1:
                LGesamt_m   = LGesamt/1000
                LSammler_m  = LSammler/1000
                Fabstand1_m = Fabstand1/1000
                Fabstand2_m = Fabstand2/1000
                mLeer_oS    = mLeer - mSammler
                mVoll_oS    = mLeer_oS + VRohr

                forceSammler = mSammler * 9.81
                forceLeer_oS = mLeer_oS * 9.81
                forceVoll_oS = mVoll_oS * 9.81

                loadLeer_oS = forceLeer_oS/LGesamt_m
                loadVoll_oS = forceVoll_oS/LGesamt_m

                ss = SystemElements(EA=25000, EI=5000)

                ss.add_element(location=[[0, 0], [LSammler_m, 0]])
                ss.add_element(location=[[LSammler_m, 0], [
                               (Fabstand1_m+LSammler_m), 0]])
                ss.add_element(location=[
                               [(Fabstand1_m+LSammler_m), 0], [(Fabstand2_m+Fabstand1_m+LSammler_m), 0]])

                ss.add_support_hinged(node_id=[2, 3, 4])

                ss.point_load(Fy=-forceSammler, node_id=1)
                ss.q_load(q=-loadLeer_oS, element_id=2)
                ss.q_load(q=-loadLeer_oS, element_id=3)

                ss.solve()

                post.F12Leer = abs(
                    round(ss.reaction_forces[2].Fz/100, 0)*100)/2
                post.F34Leer = abs(
                    round(ss.reaction_forces[3].Fz/100, 0)*100)/2
                post.F56Leer = abs(
                    round(ss.reaction_forces[4].Fz/100, 0)*100)/2

                ss.q_load(q=-loadVoll_oS, element_id=2)
                ss.q_load(q=-loadVoll_oS, element_id=3)

                ss.solve()

                post.F12Voll = abs(
                    round(ss.reaction_forces[2].Fz/100, 0)*100)/2
                post.F34Voll = abs(
                    round(ss.reaction_forces[3].Fz/100, 0)*100)/2
                post.F56Voll = abs(
                    round(ss.reaction_forces[4].Fz/100, 0)*100)/2

            post.save()
            return redirect('statics:static6F')

        args = {'form': form}
        return render(request, self.template_name, args)

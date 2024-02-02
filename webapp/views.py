from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *


def index(request):
    members = Member.objects.all()
    programs = Program.objects.all()
    total_members = members.count()
    total_programs = programs.count()

    context = {
        'members': members,
        'total_members': total_members,
        'programs': programs,
        'total_programs': total_programs

    }
    return render(request,  'pages/homepage.html', context)

def aboutPage(request):
    return render(request,  template_name='pages/aboutpage.html')

def login(request):
    return render(request,  template_name='pages/login.html')

def program(request):
     programs = Program.objects.all()

     context = {
        'programs': programs,
    }
     return render(request,  'pages/program.html', context)
 
def program_create(request):
    programForm = ProgramForm
    
    if request.method == 'POST':
        programForm = ProgramForm(request.POST)
        if programForm.is_valid():
            programForm.save()
            return redirect(to="program_page")
        programForm = ProgramForm(request.POST)
    
    context = {
        'programForm' : programForm
    }
    return render(request, 'pages/program_create.html', context)


def program_edit(request, programID):
    program = Program.objects.get(id=programID)
    programForm = ProgramForm(instance=program)
    
    if request.method == 'POST':
        programForm = ProgramForm(request.POST, instance=program)
        programForm.save()
        return redirect(to="program_page")

        
    
    context = {
        'program' : program, 
        'programForm' : programForm
    }
    
    return render(request, 'pages/program_edit.html', context)


def program_delete(request, programID):
    program = Program.objects.get(id=programID)
    program.delete()
    return redirect(to="program_page")

def member(request):
    members = Member.objects.all()

    context = {
        'members': members,

    }
    return render(request, 'pages/member.html', context)

def programmemberslist(request):
   members = Member.objects.all()

   context = {
        'members' : members,

    }
   return render(request,  'pages/programmemberslist.html', context)

def userslist(request):
    return render(request, template_name='pages/userslist.html')



def create_member(request):
    if request.method == 'POST':
        form = MemberCreationForm(request.POST)
        if form.is_valid():
            member = form.save()
            
            return redirect('programmemberslist_page')  
    else:
        form = MemberCreationForm()

    return render(request, 'pages/create_member.html', {'form': form})

def edit_member(request, membership_number):
    member = get_object_or_404(Member, membership_number=membership_number)

    if request.method == 'POST':
        form = MemberCreationForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('programmemberslist_page')  
    else:
        form = MemberCreationForm(instance=member)

    return render(request, 'pages/edit_member.html', {'form': form, 'member': member})

def delete_member(request, membership_number):
    member = get_object_or_404(Member, membership_number=membership_number)

    if request.method == 'POST':
        member.delete()
        return redirect('programmemberslist_page')

    return render(request, 'pages/delete_member.html', {'member': member})
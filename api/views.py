from django.shortcuts import render, get_object_or_404, redirect
from .models import UserAccount
from .forms import UserAccountForm

# 1. LIST (Liste)
def user_list(request):
    users = UserAccount.objects.all().order_by('-created_at')
    return render(request, 'api/user_list.html', {'users': users})

# 2. READ (Détail)
def user_detail(request, pk):
    user = get_object_or_404(UserAccount, pk=pk)
    return render(request, 'api/user_detail.html', {'user': user})

# 3. CREATE (Création)
def user_create(request):
    if request.method == 'POST':
        form = UserAccountForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserAccountForm()
    return render(request, 'api/user_form.html', {'form': form, 'title': 'Créer un utilisateur'})

# 4. UPDATE (Modification)
def user_update(request, pk):
    user = get_object_or_404(UserAccount, pk=pk)
    if request.method == 'POST':
        form = UserAccountForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserAccountForm(instance=user)
    return render(request, 'api/user_form.html', {'form': form, 'title': 'Modifier l\'utilisateur', 'user': user})

# 5. DELETE (Suppression)
def user_delete(request, pk):
    user = get_object_or_404(UserAccount, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'api/user_confirm_delete.html', {'user': user})
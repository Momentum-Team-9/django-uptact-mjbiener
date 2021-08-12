from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact, Note
from .forms import ContactForm, NoteForm, NewNoteForm


# Create your views here.
def list_contacts(request):
    contacts = Contact.objects.all()
    return render(request, "contacts/list_contacts.html",
                  {"contacts": contacts})


def add_contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_contacts')

    return render(request, "contacts/add_contact.html", {"form": form})


def edit_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'GET':
        form = ContactForm(instance=contact)
    else:
        form = ContactForm(data=request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect(to='list_contacts')

    return render(request, "contacts/edit_contact.html", {"form": form,
        "contact": contact})


def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect(to='list_contacts')

    return render(request, "contacts/delete_contact.html",
                  {"contact": contact})

def view_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    notes = contact.notes.all()
    return render(request, "contacts/view_contact.html",
                  {"contact": contact, "notes": notes})

def view_notes(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    notes = contact.notes.all()
    return render(request, "contacts/view_notes.html",
                  {"contact": contact, "notes": notes})


def edit_note(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'GET':
        form = NoteForm(instance=note)
    else:
        form = NoteForm(data=request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect(to='list_contacts')

    return render(request, "contacts/edit_note.html", {
        "form": form, "note": note})


def add_note(request):
    if request.method == 'GET':
        form = NewNoteForm()
    else:
        form = NewNoteForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_contacts')

    return render(request, "contacts/add_note.html", {"form": form})
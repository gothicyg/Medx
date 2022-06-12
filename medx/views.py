from django.shortcuts import render
from .models import Book, Entry
from .forms import BookForm, EntryForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.
def index(request):
    """The home page for medx"""
    return render(request, 'medx/index.html')
@login_required
def books(request):
    """Shows all books."""
    books = Book.objects.filter(owner=request.user).order_by('date_added')
    context = {'books': books}
    return render(request, 'medx/books.html', context)
@login_required
def book(request, book_id):
    """Show a single book and all its entries. """
    book = Book.objects.get(id=book_id)
    #make sure the book belongs to the current user.
    if book.owner != request.user:
        raise Http404
    entries = book.entry_set.order_by('-date_added')
    context = {'book': book, 'entries': entries}
    return render(request, 'medx/book.html', context)
@login_required
def new_book(request):
    """Add a new book"""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BookForm()
    else:
        # POST data submitted; process data.
        form =BookForm(data=request.POST)
        if form.is_valid():
            new_book = form.save(commit=False)
            new_book.owner = request.user
            new_book.save()
            return redirect('medx:books')
    #display a blank or invalid form.
    context = {'form':form}
    return render(request, 'medx/new_book.html', context)
@login_required
def new_entry(request, book_id):
    """Add a new entry for a particular book."""
    book = Book.objects.get(id=book_id)
    if request.method != 'POST':
       # No data submitted; create a blank form.
       form = EntryForm()
    else:
        # Post data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.book = book
            new_entry.save()
            return redirect ('medx:book', book_id=book_id)
    # Display a blank or invalid form.
    context = {'book':book, 'form':form}
    return render(request, 'medx/new_entry.html', context)
@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    book = entry.book
    if book.owner != request.user:
        raise Http404

    if request.method != 'POST':
        #Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        #Post data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('medx:book', book_id=book.id)

    context = {'entry':entry, 'book':book, 'form':form}
    return render(request, 'medx/edit_entry.html', context)













    
    
    

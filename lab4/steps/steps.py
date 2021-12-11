# -*- coding: utf-8 -*-
from Library import*
from behave import given, when, then

@given(u'There is an English book named "{bookName}"')
def step_impl(context, bookName:str):
    context.book=EnglishBook(bookName)

@given(u'There is an English reader')
def step_impl(context):
    context.reader=EnglishReader()


@given(u'There is a Russian book named "{bookName}"')
def step_impl(context, bookName: str):
    context.book = RussianBook(bookName)

@given(u'There is a Russian reader')
def step_impl(context):
    context.reader = RussianReader()


@when(u'The reader tries to read the book')
def step_impl(context):
    context.result=context.reader.read_a_book(context.book)


@then(u'The next result is expected: "{result}"')
def step_impl(context, result):
    assert context.result==result

@when(u'The book is translated')
def step_impl(context):
    context.book=TranslatorToRussian(context.book).translate()
    context.result=context.book.name
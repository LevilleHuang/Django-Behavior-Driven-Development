from behave import then, when
from behave_django.environment import PatchedContext


@when(u'I visit the home page')
def visit_web(context: PatchedContext):
    url = context.get_url("/home/")
    context.response = context.test.client.get(url)


@then(u'it is avaiable')
def page_workers(context: PatchedContext):
    context.test.assertEqual(context.response.status_code, 200)

@then(u'it provides a salutation document')
def page_contains_salutation_document(context: PatchedContext):
    context.test.assertContains(context.response, "Hello!")
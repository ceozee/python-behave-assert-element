from behave import given, when, then
from requests import get
from assertpy import assert_that


@given('an api url with valid response')
def step_imp(context):
    context.get_url = 'https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false'


@when('user sends request to get response')
def step_imp(context):
    context.response = get(context.get_url)


@then('it should display Name with value Carbon credits')
def step_imp(context):
    assert_that(context.response.status_code).is_equal_to(200)
    response = context.response.json()
    assert_that(response['Name']).described_as('Name Value').is_equal_to('Carbon credits')


@then('it should display CanRelist with boolean value True')
def step_imp(context):
    assert_that(context.response.status_code).is_equal_to(200)
    response = context.response.json()
    assert_that(response['CanRelist']).described_as('CanRelist value').is_true()


@then('Galery Promotion should display description with value 2x larger image')
def step_imp(context):
    assert_that(context.response.status_code).is_equal_to(200)
    response = context.response.json()

    promotion_name = 'Gallery'
    promotions = response['Promotions']
    promotion_counter = len(response['Promotions'])
    counter = 0
    while counter < promotion_counter:
        if promotions[counter]['Name'] == promotion_name:
            promotion_description = promotions[counter]['Description']
        counter = counter + 1

    assert_that(promotion_description).described_as('Galery Promotion Description').contains('2x larger image')

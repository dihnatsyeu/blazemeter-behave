from behave import given, when, then


@given("the user is on the search page")
def user_on_search_page(context):
    context.web.open("http://blazedemo.com/")


@when('the user selects a departure city "{city}"')
def user_select_departure_city(context, city):
    context.web.find_by_xpath("//select[@name='fromPort']/option[text()='{}']".format(city)).click()


@when('the user selects a destination city "{city}"')
def user_select_destination_city(context, city):
    context.web.find_by_xpath("//select[@name='toPort']/option[text()='{}']".format(city)).click()


@when("clicks on the Find Flights button")
def user_clicks_on_find_flights(context):
    context.web.find_by_xpath("//input[@type='submit']").click()


@then("flights are presented on the search result page")
def flights_are_found(context):
    elements = context.web.finds_by_xpath("//table/tbody/tr")
    assert len(elements) > 1

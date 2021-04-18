import json

from flask import Flask, render_template
import requests
from operator import itemgetter

# Decorator defines a route
# http://localhost:5000/countryname/<..country name..>
app = Flask(__name__)


@app.route('/countryname/<country_name>')
# return template for country's details data
def country_details(country_name):
    try:
        result = {}  # dictionary stores the country's details as a result

        # url of the country's data
        URL = ("https://restcountries.eu/rest/v2/name/%s?fullText=true" % country_name)
        # request's response
        response = requests.get(URL)

        # invalid country name display bad request 400 message
        if response.status_code == 404:
            return "Bad request error,country name is invalid", 400

        # get the http request's response as a json object
        jsonResponse = response.json()

        # add the country's name to the result dic
        result["name"] = jsonResponse[0]["name"]

        # add the country's capital to the result dic
        result["capital"] = jsonResponse[0]["capital"]

        # convert language's name list as a string
        commonLanguages = ', '.join(map(str, list(map(itemgetter('name'), jsonResponse[0]["languages"]))))
        # add the country's languages to the result dic
        result["languages"] = commonLanguages

        # convert currencies list as a string
        currencies = ', '.join(map(str, list(map(itemgetter('name'), jsonResponse[0]["currencies"]))))
        # add the currencies to the result dic
        result["currencies"] = currencies

        rates = []
        # iterate currencies list
        # get relevant rate's url
        # add rate to rates list
        for currency in jsonResponse[0]["currencies"]:
            # get currency symbol
            currencySymbol = currency["code"]
            #  get the relevant url
            URL = (
                    "http://data.fixer.io/api/latest?access_key=0f74f9e3e64cb0c2ce6ec5230dc7592d&format=1&symbols=%s" % currencySymbol)
            # get the request's response as a json object
            jsonResponse = requests.get(URL).json()
            # add symbol(key) and rate(value) to rates list
            rates.append(currencySymbol + ": " + str(jsonResponse["rates"][currencySymbol]))
        # add the rates list as a string to the result dic
        result["rates"] = ', '.join(map(str, rates))

        # return country's details template
        return render_template('country.html', data=result)
    except json.JSONDecodeError() or ValueError:
        if jsonResponse.status_code == 204:
            return "No json content", 204
        return "No JSON object"



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

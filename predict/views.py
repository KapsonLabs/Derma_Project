from rest_framework import generics
from django.http import QueryDict
import datetime

from django.http import Http404
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import serializers
from .serializers import PredictSerializer
from rest_framework import status

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

 
import urllib.request
import json

class PredictData(APIView):

    def post(self, request):
        predict_data = PredictSerializer(data=request.data)
        if predict_data.is_valid():
            
            data_list = [[float(predict_data.data['employee'])], [float(predict_data.data['ownership'])], [float(predict_data.data['credit_history'])], [float(predict_data.data['sales'])], [float(predict_data.data['credit'])], [float(predict_data.data['turnover'])], [float(predict_data.data['age_of_business'])], [float(predict_data.data['fixed_asset_value'])], [float(predict_data.data['defaulted'])], [float(predict_data.data['business_type'])]]

            #code from damalie's script
            scaler=MinMaxScaler()
            X_scaled = scaler.fit(data_list).transform(data_list)
            # data_pred=pd.DataFrame(X_scaled)

            data = {
            "Inputs": {
                "input1":
                    [
                        {
                            'Col1': str(X_scaled[0][0]),   
                            'Col2': str(X_scaled[1][0]),   
                            'Col3': str(X_scaled[2][0]),   
                            'Col4': str(X_scaled[3][0]),   
                            'Col5': str(X_scaled[4][0]),   
                            'Col6': str(X_scaled[5][0]),   
                            'Col7': str(X_scaled[6][0]),   
                            'Col8': str(X_scaled[7][0]),   
                            'Col9': str(X_scaled[8][0]),   
                            'Col10': str(X_scaled[9][0]),   
                        }
                    ],
                },
            "GlobalParameters":  {
                }
            }

            body = str.encode(json.dumps(data))

            url = 'https://ussouthcentral.services.azureml.net/workspaces/50da1d9cd1e5469eab09313ce2d8a5c4/services/5797da28acde46c19ad03cbd8938b4a1/execute?api-version=2.0&format=swagger'
            api_key = '7/1GTEPNjebtQ4Oq3kLFZyYoXhivqCxBKbfg0L0Q6yA80oGop2s/BzWdxmUzJv8yQERZ5NKvqDzx8j8AEh6xWQ==' # Replace this with the API key for the web service
            headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

            req = urllib.request.Request(url, body, headers)

            try:
                response = urllib.request.urlopen(req)

                result = response.read()
                #decode result from binary string to dictionary
                decoded_result=json.loads(result.decode())

                scored_label = decoded_result['Results']['output1'][0]['Scored Labels']
                print(scored_label)
            except urllib.error.HTTPError as error:
                print("The request failed with status code: " + str(error.code))

                # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
                print(error.info())
                print(json.loads(error.read().decode("utf8", 'ignore')))

            return Response({"scored_label":scored_label},status=status.HTTP_201_CREATED)
        return Response(predict_data.errors, status=status.HTTP_400_BAD_REQUEST)

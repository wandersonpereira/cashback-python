import json
import requests as req
import src.cashback.types.Error as Error

class Get():
    
    def execute(document): 
        url = 'https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/cashback?cpf={}'.format(document)
        headers = {
            'token': 'ZXPURQOARHiMc6Y0flhRC1LVlZQVFRnm'
        }
        response = req.post(url, 
            headers=headers, 
            timeout=5000
        )

        if response.status_code >= 200 and response.status_code < 300:
            return {
                "data": response.json(),
                "statusCode": 200
            }
        
        return {
            "data": {"message": Error.APLICATION_ERROR},
            "statusCode": response.status_code
        }
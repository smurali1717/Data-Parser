from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from typing import Dict
from starlette.responses import JSONResponse
import json

app = FastAPI()

# Define the token URL path (not implementing OAuth2 flow, just a simple example)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Sample valid token for authentication
VALID_TOKEN = "mysecrettoken"

# Python code to hold JSON data in a dictionary

data = {
    "customers": [
        {
            "customer_name": 'Emily Davis',
            "mobile_number": '+44 1234 567890',
            "account_number": 'AC123456',
            "joined_date": '2023-08-05',
            "mobile_plan": 'Gold Plan',
            "tariff": 'Premium',
            "additional_packages": [
                {
                    "name": 'Data Boost',
                    "cost": 9.99,
                    "location": 'London',
                    "activation_date": '2023-09-10'
                }
            ],
            "package_cost": 79.99,
            "international_roaming": True,
            "additional_caps": {
                "data_cap": '25GB',
                "utilised_data": '10GB',
                "utilised_calls": '364 minutes',
                "calling_cap": '750 minutes'
            },
            "monthly_discount": 12,
            "trouble_discount": 7,
            "last_3_months_bills": [
                {
                    "month": 'January',
                    "total_bill": 84.99,
                    "breakdown": {
                        "base_plan": 79.99,
                        "additional_packages": [
                            {
                                "name": 'Data Boost',
                                "cost": 9.99
                            }
                        ],
                        "discounts": {
                            "monthly_discount": 12,
                            "trouble_discount": 7
                        }
                    }
                },
                {
                    "month": 'February',
                    "total_bill": 79.99,
                    "breakdown": {
                        "base_plan": 79.99,
                        "additional_packages": [
                            {
                                "name": 'Data Boost',
                                "cost": 9.99
                            }
                        ],
                        "discounts": {
                            "monthly_discount": 12,
                            "trouble_discount": 7
                        }
                    }
                },
                {
                    "month": 'March',
                    "total_bill": 80.99,
                    "breakdown": {
                        "base_plan": 79.99,
                        "additional_packages": [
                            {
                                "name": 'Data Boost',
                                "cost": 9.99
                            }
                        ],
                        "discounts": {
                            "monthly_discount": 12,
                            "trouble_discount": 7
                        }
                    }
                }
            ]
        }
    ]
}


# Function to verify the token
def authenticate_token(token: str = Depends(oauth2_scheme)):
    if token != VALID_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token

@app.get("/data", response_class=JSONResponse)
def get_data(token: str = Depends(authenticate_token)) :
    return data





# Run the app using: uvicorn <filename>:app --reload

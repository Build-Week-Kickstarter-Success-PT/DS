import logging
import random

from fastapi import APIRouter
import pandas as pd
from pydantic import BaseModel, Field, validator

log = logging.getLogger(__name__)
router = APIRouter()


class Item(BaseModel):
    """Use this data model to parse the request body JSON."""

    x1: float = Field(..., example=10000)
    x2: int = Field(..., example=8)
    x3: str = Field(..., example='Canada')
    x4: str = Field(..., example='Science')
    x5: str = Field(..., example='Material Thread Science')

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])

    @validator('x1')
    def x1_must_be_positive(cls, value):
        """Validate that x1 is a positive number."""
        assert value > 0, f'x1 == {value}, must be > 0'
        return value


@router.post('/predict')
async def predict(item: Item):
    """
    Eventually, this bad boy is going to predict Kickstarter success
    ### Request Body
    - `goal (x1)`: positive float
    - `campaign_length (x2)`: integer
    - `country (x3)`: string
    - `category (x4)`: string
    - `sub-category (x5)`: string
    ### Response
    - `prediction`: boolean, at random
    """

    X_new = item.to_df()
    log.info(X_new)
    def will_it_work():
        y_pred = random.choice([True, False])
        if (y_pred == True):
            return 1
        else:
            return 0 
    y_pred_proba = random.random() / 2 + 0.5
    #This is the JSON we will pass on to the front end
    return {
        'prediction': will_it_work(),
        # 'probability': y_pred_proba
    }
import config 
import argparse
import pandas as pd
from utils.analitic_utils import check_empty_values,plot
import mlflow

mlflow.set_tracking_uri("http://mlflow_service:5000")


def main(path:str):
    with mlflow.start_run():
        df=pd.read_csv(path)
        df["date"]=pd.to_datetime(df['date'])
        check_empty_values(df)
        plot(df)
  


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path') 
    args = parser.parse_args()
    main(path=args.path)
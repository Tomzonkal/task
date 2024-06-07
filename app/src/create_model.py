import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

mlflow.set_tracking_uri("http://mlflow_service:5000")

def train_model():
    # Load dataset
    data = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)

    # Train a decision tree classifier
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    # Log the model with MLflow
    with mlflow.start_run():
        mlflow.sklearn.log_model(model, "decision_tree_model")

    registered_model_name = "decision_tree_model"

    mlflow.register_model(registered_model_name,name="my_model")

if __name__ == '__main__':
    train_model()

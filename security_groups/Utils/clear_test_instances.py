import requests
from Locators.locators import EC2BaseLocators

def delete_security_group(id):
    if not id:
        print("Can't delete sec group. ID not provided")
        return False
    url = "https://console.engineering.vng.vn/api/client/security-groups"
    user_token = EC2BaseLocators.AUTOTEST_USER_TOKEN
    headers = {
        "cookie": f"user-token={user_token}",
        "accept": "application/json"
    }
    params = {
        "id": id
    }
    r = requests.delete(url, headers=headers, params=params)
    print("Secruity group delete status")
    print(r.status_code)
    print(r.content)

#
# if __name__ == '__main__':
#     ids = ["ba9bb072-0a6c-4e2b-b87d-6c35f69f7899","ba9bb072-0a6c-4e2b-b87d-6c35f69f7899","b92bc3bd-d07c-40a9-8be2-97270e1e3814","7330bf58-2174-4306-83cc-826a3ab28a26","fb6b0cd4-e166-43e2-a8cd-25848acd7055","d497ac9d-f79b-4242-88b3-65b22138c0e1","35e7d06c-1fd8-4318-a566-9949604ebb13","c68e1f23-6727-4b53-b366-d8106976bd30","1faa66a9-510d-42af-b016-61d3c525dd40","aeb7f59e-8bd6-469e-a77d-8031575a0997","3ff06b48-7a3e-4015-b6d3-803be9befd23","5e1666e0-d81c-4d5b-a826-5564ab62628d","e40d0d15-b874-41bc-980d-5b667fb1fe21","4c83a5b1-417d-4110-8c3d-5d9931ee7727","354e561c-be04-4fbd-a031-61497c8bbf84","c3ed4e1c-94b4-4472-9b97-82cfbe8643ee","4a02805d-4eb4-4a70-a84d-4f1bedbea6ae","c0401271-dfba-4418-b19c-c6ebe37a59d9","afa1cbb8-a686-486c-a0c5-5bdd98060da6","84b632e5-a2ec-48a1-9b04-16a8a4a96a1f","52357e47-1974-4cd0-bf14-975276f775bf",]
#     for id in ids:
#         delete_security_group(id)
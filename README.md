# Flow test bằng Selenium cho EP

## 1. Chạy flow test
###1.1 Cài thư viện cần thiết

```
pip install -r requirements.txt
```
###1.2 Chỉnh sửa user-token

- Vào ```cd Configs/local```. chỉnh sửa biến USER_TOKEN thành token của mình.

###1.3 Chạy code

####a. Chạy all test
```
python3 -m unittest -v
```
Lệnh này sẽ tìm và chạy file toàn bộ project theo các bước:
- Những file có pattern là test_*.
- Những class có pattern là Test_*, class phải kế thừa unittest.TestCase
- Những function trong class tên có pattern là test_*

<b>Note:</b> Ở project này, các file này nằm trong folder Tests 

####b. Chạy riêng 1 file test
Ví dụ chạy 1 test case Create Bucket của s3
```
python3 -m unittest Tests.s3.test_create_bucket_001 -v
```
####c. Chạy các file test trong 1 folder
Ví dụ chạy các file toàn bộ test s3
```
python3 -m unittest discover Tests.s3 -v
```

<b>Debug</b>: Hiện tại các flow đang là headless-test, tức là ko hiện browser để mình nhìn.
Để tiện debug, vào chỗ khai báo driver (ở các class Base), comment dòng này lại:
```chrome_options.add_argument('--headless')``` hoặc ```options.headless = True```.

##2. Project Structure
* ###Configs
    * <b>Configs/TestData</b>: Chứa các plain text trên UI để test.
    * <b>Configs/\*.py</b>: Chứa các configs url, token,...*
  
* ###Driver
    * Chứa các driver của browser
* ###Locators
    * Chứa các biến để define các địa chỉ để định vị các element trong 1 trang.
    * Tham khảo: https://selenium-python.readthedocs.io/locating-elements.html
* ### Pages
    * Chứa các biến, function thuộc 1 page, ví dụ click vào 1 nút, điền thông tin
    vào 1 textbox,... Khi test, các hành động sẽ được gọi qua các module page này.
    * Các page này sẽ định vị các web element của page qua Locators.  
* ### Tests
    * Các module test chính. Các test thực hiện các action trên page qua module Pages.
    Sau đó dùng các hàm assert của unittest để kiểm tra các điều kiện mình expect trên
      1 page. Nếu 1 trong các assert không thoả mãn, coi như test case đó faiil.
    

## 3. Tài liệu tham khảo
- Docs Selenium step by step: https://selenium-python.readthedocs.io/index.html
- Example flow test cơ bản: https://realpython.com/headless-selenium-testing-with-python-and-phantomjs/
- Design patterns - POM: https://www.lambdatest.com/blog/page-object-model-in-selenium-python/
- Design patterns - POM: https://medium.com/@asheeshmisra29/web-automation-selenium-webdriver-and-python-getting-started-part-3-a9c07143d36d


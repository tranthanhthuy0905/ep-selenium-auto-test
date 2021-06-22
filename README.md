# Flow test bằng Selenium cho EP
## 1. Tóm tắt flow test
Mục đích của task này là sử dụng Selenium để hiện thực web browser, truy cập vào EP, thao tác theo các scenario mình mong muốn.
Kết quả thành công/thất bại của một thao tác do mình tự define, và kết quả này sẽ phải được alert hoặc log lại.

Ví dụ 1 scenario - Selenium tạo bucket s3 qua các bước sau:
1. Dựng web browser lên
2. Truy cập vào https://s3.engineering.vng.vn/s3/
3. Thực hiện thao tác đăng nhập qua token. Kết quả nếu thành công, url hiện tại sẽ là https://s3.engineering.vng.vn, ko thì coi như thất bại.
4. Chọn nút "Create Bucket". Nếu thành công, url hiện tại sẽ là https://s3.engineering.vng.vn/s3/buckets/create; Thấy được header "Create Bucket"; Có đủ 2 text box,...
5. Điền thông tin vào 2 text box
6. Chọn nút "Create Bucket". Nếu thành công, url sẽ là https://s3.engineering.vng.vn/s3/buckets/<tên-bucket>; Display được 1 số text nhất định ở trang tạo thành công.


## 2. Legacy code (code cũ)
#### Các thư viện cần: 
```
selenium
webdriver-manager
```
Code cũ đã có sơ lược 3 service. Các services này base code ko dính dáng gì đến nhau, nên mọi người cứ tham khảo qua hết flow. 2 base code "gần chuẩn" theo **Page Object Model** design pattern là security_groups với ec2 instance.
1. ec2 instance: ./test_instances
   ```
   cd test_instances
   bash run.sh
   ```
2. ec2 security group: ./security_groups
   ```
   cd security_groups
   python3 -m Tests.security_groups
   bash run.sh
   ```
3. s3: ./ep-storage_headless
    ```
   cd ep-storage_headless/sa
   python3 saFlow.py
   bash run.sh
   ```
   
#### Notes: 
Hiện tại các flow đang là headless-test, tức là ko hiện browser để mình nhìn. 
Để tiện debug, mọi người vào chỗ khai báo driver (ở các class Base), comment dòng này lại:
```chrome_options.add_argument('--headless')```.

## 3. Tài liệu tham khảo
- Docs Selenium step by step: https://selenium-python.readthedocs.io/index.html
- Example flow test cơ bản: https://realpython.com/headless-selenium-testing-with-python-and-phantomjs/
- Design patterns - POM: https://www.lambdatest.com/blog/page-object-model-in-selenium-python/
- Design patterns - POM: https://medium.com/@asheeshmisra29/web-automation-selenium-webdriver-and-python-getting-started-part-3-a9c07143d36d


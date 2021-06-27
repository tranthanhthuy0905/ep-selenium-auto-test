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


## 2. Chạy flow test
#### Notes: 
- Debug: Hiện tại các flow đang là headless-test, tức là ko hiện browser để mình nhìn.
Để tiện debug, vào chỗ khai báo driver (ở các class Base), comment dòng này lại:
```chrome_options.add_argument('--headless')``` hoặc ```options.headless = True```.
- Authentication: Phần authentication nằm ở hàm add_cookie sau khi init driver. Chỉnh biến cookie, field value thành token mới nhất. Payload cookie:
```{"name": "user-token", "value": "<user-token>"}```
```
pip install -r requirements.txt
python3 -m unittest -v
```

## 4. Tài liệu tham khảo
- Docs Selenium step by step: https://selenium-python.readthedocs.io/index.html
- Example flow test cơ bản: https://realpython.com/headless-selenium-testing-with-python-and-phantomjs/
- Design patterns - POM: https://www.lambdatest.com/blog/page-object-model-in-selenium-python/
- Design patterns - POM: https://medium.com/@asheeshmisra29/web-automation-selenium-webdriver-and-python-getting-started-part-3-a9c07143d36d


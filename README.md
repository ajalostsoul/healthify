# healthify

Note: Please dont mind my css because i havent used one (P.S i applied for backend dev post)<br>

Testing Steps:<br>
1. Just copy the full package including manage.py and all the folders<br>
2. set up a local server using manage.py runserver<br>
3. hit the url localhost:8000<br>
4. Click on create question by giving admin email "ankijai+setter1@gmail.com" <br>
5. After this come back to home and signup <br>
6. give vote and then using admin interface (/admin) , in the voters table you can see the vote.<br>

Testcases and scenarios covered:<br>
1. Internal links should not be accessible directly (used session based approach)<br>
2. Form field validation (Empty fields, Email validation etc)<br>
3. Same user should not be allowed to give vote again even in other browser.<br>
4. Question should be updated in DB when admin puts new question.<br>
5. User should land on apt pages on hitting internal url's eg: if an user is hitting /quiz/ url (which is voting page) ,if she is not loggedin the she should land on signup page.<br>
6. Apt msgs should be displayed on errors.<br>
7. Kindly explore the app to know more.<br>


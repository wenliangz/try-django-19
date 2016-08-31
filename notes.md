# 1. Model (model.py)
- Define a Model in Django

# 2. Django(Admin App) View for managing data in Model: (admin.py)
Edit application’s models in the admin interface.
- register user model
- customize user model by defining a class
- this view is for the administrator to use; designed and contributed by Django
- the view on the admin site could be served as mimic to create our own view
- URL: /admin/

# 3. Our own View for managing data data in Model: (view.py)
- this view is for the end user to use
- URL is controled by controller (URL.py)
- Model View Controller (MVC)
- CRUD: 
    - CREATE -- POST --Make new
    - RETRIEVE -- GET -- List/Search
    - UPDATE -- PUT/PATCH --EDIT
    - DELETE -- DELETE --delete
- Create first View
- Request&Response Cycle
    - Request: User click a link on web(different link may have different request)  -- knock the door
        - GET; POST;PUT; DELETE
    - Resposne: Sever returns a response  -- answer the door
- View functions is what the server use to handle the request and return response; so the view function always take request object and return response object(most of the time, the type of response is HttpResponse)
-  URL.py is used to map each request(url link) to the corresponding view function for handling
    
# 4. Mapping URLs to Views
- two ways of writing url mapping
    - absolute path, better
    - potential problems with multile apps with multiple views; can use "import view as"
    - In App Views: 
        - use include function in the main url.py; 
        - create and define each app's own url.py in each app folder
        - notice: no '$' sign at the end of url pattern in main folder, in order to delegate the pattern to the app's url patten 
     
    
    
    
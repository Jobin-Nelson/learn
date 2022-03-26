# ASP.NET Core
- It is a cross platform, high performance open source Web framework
- It is used to build modern, internet connected apps

## Approaches for building web apps
- Server rendered UI
	- for static pages
- Client rendered UI
	- for interactive dashboards, collaborative apps
- Hybrid 

## Server rendered UI
- **Razor Pages**
	- Page based model where the UI and business logic concerns are kept seperate
	- Easy to test and scale
- **MVC** (Model View Controller)
	- This pattern seperates the app into Models, Views and Controllers
	- Controller uses the model to perform user actions and uses views to display the UI
	- Great for building large scalable apps

## Client rendered UI
- **Blazor**
	- Blazor apps are composed of Razor components
	- We create segments of reusbale codes in C#, HTML and CSS
- **SPA** (Single Page Application) 
	- Build client-side logic with JavaScript Frameworks such as Angular and React
	- evolving JavaScript Frameworks this can be hard to maintain

### Model View Controller
- MVC is a software design pattern used for developing user interfaces dividing the program logic into three interconnected elements
	- Model: Contains the data represented by the View
	- View: Responsible for presenting the model and handling user interactions
	- Controller: Manages the presentation and the Model


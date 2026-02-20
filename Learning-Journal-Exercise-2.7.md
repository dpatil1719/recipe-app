# Learning Journal — Exercise 2.7
## Data Analysis and Visualization in Django

---

## What I Learned

In this exercise, I learned how to enhance a Django application by adding data analysis and visualization features.

I understood how to:

- Build a search feature using Django forms
- Filter database records using partial matching with icontains
- Use pandas to convert query results into a table format
- Generate charts using matplotlib
- Embed charts inside Django templates using base64 encoding
- Protect views using authentication

---

## Key Concepts Learned

### 1. Django Forms
I learned how to create a custom form using Django's forms module. The form allowed users to:

- Enter a recipe name to search
- Select a chart type (bar, pie, or line)

This helped me understand how forms collect and validate user input.

---

### 2. Database Filtering

I learned how to search the database dynamically using:

Recipe.objects.filter(name__icontains=keyword)

This was important because:

- It allows partial text search
- It is case-insensitive
- It makes search functionality flexible

---

### 3. Using Pandas in Django

This exercise introduced me to pandas for data analysis.

I learned how to:

- Convert Django querysets into DataFrames
- Display data as HTML tables using:

df.to_html()

This helped me understand how backend data can be transformed before displaying.

---

### 4. Data Visualization with Matplotlib

I learned how to generate different charts:

Bar chart — compares cooking times  
Pie chart — shows proportion of cooking times  
Line chart — shows trends  

I also learned how to convert charts into base64 images so they can be displayed in web pages.

---

### 5. Base64 Image Rendering

One of the most interesting parts was learning how to:

- Save a chart to memory using BytesIO
- Convert it into a base64 string
- Embed it directly into HTML

This avoids storing images physically on disk.

---

### 6. Authentication Protection

I learned how to secure pages using:

LoginRequiredMixin  
@login_required decorator  

This ensures only logged-in users can access recipes and search features.

---

## Challenges I Faced

I encountered several issues during this exercise:

- Indentation errors in Python files
- Form field mismatches
- Query errors when search input was empty
- Chart rendering issues with incorrect plotting

I resolved these problems by:

- Carefully checking indentation
- Using cleaned_data from forms
- Validating form inputs
- Debugging step-by-step

---

## Testing Knowledge

I ran Django automated tests and learned:

- How Django creates a temporary test database
- How unit tests verify functionality automatically
- The importance of passing all tests before submission

All tests passed successfully.

---

## Overall Learning Experience

This exercise was very important because it helped me understand how a real web application works end-to-end:

User input → Backend processing → Data analysis → Visualization → Display

It also improved my debugging skills and confidence in using Django, pandas, and matplotlib together.

---

## Conclusion

By completing this exercise, I gained hands-on experience in:

- Building search functionality
- Performing data analysis in web apps
- Creating dynamic visualizations
- Protecting application routes

This exercise significantly strengthened my full-stack development skills.


<h1>Employee App</h1>

<h2>Project Description</h2>

<p>The Employee Management System is a web-based application designed to simplify and streamline the process of managing employee data within an organization. It provides an intuitive interface for the management department to efficiently add, edit, and delete employee records, including their salaries and positions.</p></br>

<h3>Key Features</h3>
<ul>
  <li>
    <p><b>Employee Database:</b> The system serves as a centralized database to store comprehensive employee information, such as employee ID, name, contact details, start date, position, and     salary.</p>
  </li>
  <li>
    <p><b>User-friendly Interface:</b> The application offers a user-friendly interface, making it easy for management personnel to navigate through the system and perform various actions with         minimal effort.</p>
  </li>
  <li>
    <p><b>Employee Addition:</b> The system allows the addition of new employees by entering their relevant details, ensuring accurate and up-to-date employee records.</p>
  </li>
  <li>
    <p><b>Employee Editing: </b> Management personnel can update employee details, such as salary and position, as needed. The system ensures that changes are           reflected accurately across the database.</p>
  </li>
  <li>
    <p><b>Employee Deletion: </b> The application enables the deletion of employee records when required, ensuring the removal of outdated or redundant information       from the database.</p>
  </li>
</ul>

<h3>Installation</h3>

<p>1. Clone the project repository from GitHub:</p>
<p><b>git clone "repository_url"</b></p>

<p>2. Navigate to the project directory:</p>
<p><b>cd employees</b></p>

<p>3. Install the required Python packages:</p>
<p><b>pip install -r requirements.txt</b></p>

<p>4. Configure the Database:</p>
<ul>
  <li>
    <p>Open the settings.py file located in the employee_management_system directory.</p>
  </li>
</ul>
<ul>
  <li>
    <p>Update the DATABASES settings according to your database configuration, including the database name, username, password, host, and port.</p>
  </li>
</ul>

<p>5. Run database migrations to create the necessary tables:</p>
<p><b>python manage.py migrate</b></p>

<p>6. (Optional) If you have an Excel file with employee data, you can import it to the database using the following command:</p>
<p><b>python manage.py import_employees "path_to_excel_file"</b></p>

<p>7. Start the development server:</p>
<p><b>python manage.py runserver</b></p>

<p>8. Open a web browser and navigate to http://localhost:8000 to access the Employee Management System. Note: The port number may vary depending on your Django configuration.</p>

<p>9. You can now add, edit, and delete employees, manage their salaries and positions, and leverage the features provided by the Employee Management System.</p>

<h3>Technologies Used</h3>
<ul>
  <li>Python</li>
  <li>Django</li>
  <li>HTML</li>
  <li>CSS</li>
  <li>Bootstrap</li>
</ul>

<h3>Authors</h3>
<p>Denis Bechiragich</p>

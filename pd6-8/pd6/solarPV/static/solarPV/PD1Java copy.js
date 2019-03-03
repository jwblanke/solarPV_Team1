var username_check = false;
var firstname_check = false;
var middlename_check = false;
var lastname_check = false;
var gender_check = false;
var address_check = false;
var city_check = false;
var state_check = false;
var zipcode_check = false;
var email_check = false;
var number_check = false;
var company_check = false;

function checkUsername(username)
{
    if (!username_check)
    {
        var usernameAlert = document.getElementById(username);
        if (!usernameAlert.value)
        {
            window.alert("Must enter a Username");
            usernameAlert = document.getElementById(username);
        }
    }
    else 
    {
        return true;
    }
};

function checkPassword(password)
{
    if (!password_check)
    {
        var passwordAlert = document.getElementById(password);
        if (!passwordAlert.value)
        {
            window.alert("Must enter a Password");
            passwordAlert = document.getElementById(password);
        }
    }
    else {}
};

function checkFirstName(firstname)
{           
    if (!firstname_check)
    {
        var firstnameAlert = document.getElementById(firstname);
        if (!firstnameAlert.value)
        {
            window.alert("Must enter a First Name");
            firstnameAlert = document.getElementById(firstname);
        }
    }
    else {}
};

function checkMiddleName(middlename)
{           
    if (!middlename_check)
    {
        var middlenameAlert = document.getElementById(middlename);
        if (!middlenameAlert.value)
        {
            window.alert("Must enter a Middle Name");
            middlenameAlert = document.getElementById(middlename);
        }
    }
    else {}
};

function checkLastName(lastname)
{           
    if (!lastname_check)
    {
        var lastnameAlert = document.getElementById(lastname);
        if (!lastnameAlert.value)
        {
            window.alert("Must enter a Last Name");
            lastnameAlert = document.getElementById(lastname);
        }
    }
    else {}
};

function checkGender(gender)
{           
    if (!gender_check)
    {
        var genderAlert = document.getElementById(gender);
        if (!genderAlert.value)
        {
            window.alert("Must enter a gender");
            genderAlert = document.getElementById(gender);
        }
    }
    else {}
};
    
function checkAddress(address)
{           
    if (!address_check)
    {
        var addressAlert = document.getElementById(address);
        if (!addressAlert.value)
        {
            window.alert("Must enter an address");
            addressAlert = document.getElementById(address);
        }
    }
    else {}
};

function checkCity(city)
{           
    if (!city_check)
    {
        var cityAlert = document.getElementById(city);
        if (!cityAlert.value)
        {
            window.alert("Must enter a city");
            cityAlert = document.getElementById(city);
        }
    }
    else {}
};

function checkState(state)
{           
    if (!state_check)
    {
        var stateAlert = document.getElementById(state);
        if (!stateAlert.value)
        {
            window.alert("Must enter a state");
            stateAlert = document.getElementById(state);
        }
    }
    else {}
};

function checkZipcode(zipcode)
{           
    if (!zipcode_check)
    {
        var zipcodeAlert = document.getElementById(zipcode);
        if (!zipcodeAlert.value)
        {
            window.alert("Must enter a zipcode");
            zipcodeAlert = document.getElementById(zipcode);
        }
    }
    else {}
};

function checkEmail(email)
{           
    if (!email_check)
    {
        var emailAlert = document.getElementById(email);
        if (!emailAlert.value)
        {
            window.alert("Must enter a email");
            emailAlert = document.getElementById(email);
        }
    }
    else {}
};

function checkNumber(number)
{           
    if (!number_check)
    {
        var numberAlert = document.getElementById(number);
        if (!numberAlert.value)
        {
            window.alert("Must enter a telephone number");
            numberAlert = document.getElementById(number);
        }
    }
    else {}
};

function checkCompany(company)
{           
    if (!company_check)
    {
        var companyAlert = document.getElementById(company);
        if (!companyAlert.value)
        {
            window.alert("Must enter a company");
            companyAlert = document.getElementById(company);
        }
    }
    else {}
};

function confirmation ()
{
    window.alert("You are now registered.");
    return true;
}
    
function verifyAll()
{
    checkUsername()
    checkPassword()
    checkFirstname()
    checkMiddlename()
    checkLastname()
    checkGender()
    checkAddress()
    checkCity()
    checkState()
    checkZipcode()
    checkEmail()
    checkNumber()
    checkCompany()   
};
import streamlit as st
import pandas as pd
import re
from datetime import datetime
import random

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Donate Life AI",
    page_icon="❤️",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

.main{
    background:#020617;
    color:white;
}

.title{
    text-align:center;
    font-size:60px;
    font-weight:bold;
    color:#ff4b4b;
}

.subtitle{
    text-align:center;
    color:#cbd5e1;
    font-size:22px;
    margin-bottom:30px;
}

.card{
    background:#111827;
    padding:20px;
    border-radius:15px;
    margin-bottom:20px;
}

.stButton>button{
    width:100%;
    background:#ff4b4b;
    color:white;
    border:none;
    border-radius:12px;
    padding:12px;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#dc2626;
}

</style>
""", unsafe_allow_html=True)

# ---------------- DATABASE ---------------- #

if "donors" not in st.session_state:
    st.session_state.donors = []

if "patients" not in st.session_state:
    st.session_state.patients = []

# ---------------- VALIDATIONS ---------------- #

VALID_CITIES = [
    "Hyderabad",
    "Vijayawada",
    "Visakhapatnam",
    "Warangal",
    "Tirupati"
]

VALID_HOSPITALS = [
    "Apollo Hospital",
    "Yashoda Hospital",
    "KIMS Hospital",
    "Care Hospital",
    "Rainbow Hospital"
]

ORGANS = [
    "Kidney",
    "Heart",
    "Liver",
    "Lungs",
    "Eyes"
]

BLOOD_GROUPS = [
    "A+","A-","B+","B-",
    "O+","O-","AB+","AB-"
]

def valid_name(name):
    return bool(re.fullmatch(r"[A-Za-z ]{3,50}", name))

def valid_phone(phone):
    return bool(re.fullmatch(r"\d{10}", phone))

def valid_email(email):
    return bool(re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email))

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("❤️ Donate Life AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Login",
        "Donor Registration",
        "Patient Registration",
        "Live Match System",
        "Emergency Request",
        "Admin Dashboard",
        "Awareness",
        "FAQ",
        "About"
    ]
)

# ---------------- HOME PAGE ---------------- #

if page == "Home":

    st.markdown(
        '<p class="title">❤️ Donate Life AI</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="subtitle">AI Powered Organ Donation Platform</p>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Registered Donors", len(st.session_state.donors))
    col2.metric("Patients", len(st.session_state.patients))
    col3.metric("Lives Saved", random.randint(20, 100))

    st.success("Together We Can Save Lives ❤️")

    st.image(
        "https://www.shutterstock.com/image-vector/donation-organs-doctors-hands-hold-260nw-1564019128.jpg",
        use_container_width=True
    )

# ---------------- LOGIN PAGE ---------------- #
# ---------------- USER DATABASE ---------------- #

if "users" not in st.session_state:

    st.session_state.users = [
        {
            "Name": "Admin",
            "Login": "admin",
            "Password": "admin123"
        }
    ]

if "generated_otp" not in st.session_state:
    st.session_state.generated_otp = ""

# ---------------- LOGIN / SIGNUP PAGE ---------------- #

elif page == "Login":

    st.markdown(
        '<p class="title">Secure Login & Signup</p>',
        unsafe_allow_html=True
    )

    auth_option = st.radio(
        "Choose Option",
        ["Login", "Sign Up"]
    )

    # ---------------- SIGNUP ---------------- #

    if auth_option == "Sign Up":

        st.subheader("Create New Account")

        signup_name = st.text_input(
            "Full Name"
        )

        signup_input = st.text_input(
            "Email OR Phone Number"
        )

        signup_password = st.text_input(
            "Create Password",
            type="password"
        )

        if st.button("Generate OTP"):

            if (
                valid_email(signup_input)
                or valid_phone(signup_input)
            ):

                otp = str(random.randint(1000, 9999))

                st.session_state.generated_otp = otp

                st.success(
                    f"OTP Generated: {otp}"
                )

            else:

                st.error(
                    "Enter Valid Email or Phone Number"
                )

        signup_otp = st.text_input(
            "Enter OTP"
        )

        if st.button("Create Account"):

            if (
                signup_otp
                == st.session_state.generated_otp
            ):

                st.session_state.users.append({
                    "Name": signup_name,
                    "Login": signup_input,
                    "Password": signup_password
                })

                st.success(
                    "Account Created Successfully ✅"
                )

            else:

                st.error("Invalid OTP")

    # ---------------- LOGIN ---------------- #

    else:

        st.subheader("User Login")

        login_input = st.text_input(
            "Email OR Phone Number"
        )

        login_password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            user_found = False

            for user in st.session_state.users:

                if (
                    user["Login"] == login_input
                    and user["Password"] == login_password
                ):

                    user_found = True
                    break

            if user_found:

                st.success(
                    "Login Successful ✅"
                )

                st.balloons()

            else:

                st.error(
                    "Invalid Login Credentials"
                )
# ---------------- USER DATABASE ---------------- #

if "users" not in st.session_state:
    st.session_state.users = []

if "generated_otp" not in st.session_state:
    st.session_state.generated_otp = ""

# ---------------- LOGIN / SIGNUP PAGE ---------------- #


# ---------------- DONOR PAGE ---------------- #

elif page == "Donor Registration":

    st.markdown(
        '<p class="title">Donor Registration</p>',
        unsafe_allow_html=True
    )

    donor_name = st.text_input("Donor Name")

    donor_age = st.number_input(
        "Age",
        min_value=18,
        max_value=80
    )

    donor_phone = st.text_input(
        "Phone Number"
    )

    donor_email = st.text_input(
        "Email Address"
    )

    donor_city = st.selectbox(
        "City",
        VALID_CITIES
    )

    donor_hospital = st.selectbox(
        "Hospital",
        VALID_HOSPITALS
    )

    donor_blood = st.selectbox(
        "Blood Group",
        BLOOD_GROUPS
    )

    donor_organ = st.selectbox(
        "Organ To Donate",
        ORGANS
    )

    medical_history = st.text_area(
        "Medical History"
    )

    if st.button("Register Donor"):

        errors = []

        if not valid_name(donor_name):
            errors.append("Invalid Name")

        if not valid_phone(donor_phone):
            errors.append("Phone must be 10 digits")

        if not valid_email(donor_email):
            errors.append("Invalid Email")

        if len(medical_history.strip()) < 5:
            errors.append("Enter Medical History")

        if errors:

            for error in errors:
                st.error(error)

        else:

            donor_data = {
                "Date": datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                "Name": donor_name,
                "Age": donor_age,
                "Phone": donor_phone,
                "Email": donor_email,
                "City": donor_city,
                "Hospital": donor_hospital,
                "Blood": donor_blood,
                "Organ": donor_organ
            }

            st.session_state.donors.append(
                donor_data
            )

            st.success(
                "Donor Registered Successfully ❤️"
            )

# ---------------- PATIENT PAGE ---------------- #

elif page == "Patient Registration":

    st.markdown(
        '<p class="title">Patient Registration</p>',
        unsafe_allow_html=True
    )

    patient_name = st.text_input(
        "Patient Name"
    )

    patient_age = st.number_input(
        "Patient Age",
        min_value=1,
        max_value=100
    )

    patient_phone = st.text_input(
        "Phone Number"
    )

    patient_email = st.text_input(
        "Email Address"
    )

    patient_city = st.selectbox(
        "City",
        VALID_CITIES
    )

    patient_hospital = st.selectbox(
        "Hospital",
        VALID_HOSPITALS
    )

    patient_blood = st.selectbox(
        "Blood Group",
        BLOOD_GROUPS
    )

    needed_organ = st.selectbox(
        "Needed Organ",
        ORGANS
    )

    critical_level = st.slider(
        "Critical Level",
        1,
        10
    )

    if st.button("Register Patient"):

        errors = []

        if not valid_name(patient_name):
            errors.append("Invalid Name")

        if not valid_phone(patient_phone):
            errors.append("Phone must be 10 digits")

        if not valid_email(patient_email):
            errors.append("Invalid Email")

        if errors:

            for error in errors:
                st.error(error)

        else:

            patient_data = {
                "Date": datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
                "Name": patient_name,
                "Age": patient_age,
                "Phone": patient_phone,
                "Email": patient_email,
                "City": patient_city,
                "Hospital": patient_hospital,
                "Blood": patient_blood,
                "Needed Organ": needed_organ,
                "Critical Level": critical_level
            }

            st.session_state.patients.append(
                patient_data
            )

            st.success(
                "Patient Registered Successfully ❤️"
            )

# ---------------- LIVE MATCH SYSTEM ---------------- #

elif page == "Live Match System":

    st.markdown(
        '<p class="title">AI Match System</p>',
        unsafe_allow_html=True
    )

    if (
        len(st.session_state.donors) == 0
        or len(st.session_state.patients) == 0
    ):

        st.warning(
            "Add donors and patients first"
        )

    else:

        matches = []

        for donor in st.session_state.donors:

            for patient in st.session_state.patients:

                if (
                    donor["Organ"]
                    == patient["Needed Organ"]
                    and donor["Blood"]
                    == patient["Blood"]
                ):

                    matches.append({
                        "Donor": donor["Name"],
                        "Patient": patient["Name"],
                        "Organ": donor["Organ"],
                        "Blood Group": donor["Blood"],
                        "Hospital":
                        patient["Hospital"]
                    })

        if matches:

            st.success(
                "Matching Found ❤️"
            )

            st.dataframe(
                pd.DataFrame(matches)
            )

        else:

            st.error(
                "No Matching Found"
            )

# ---------------- EMERGENCY PAGE ---------------- #

elif page == "Emergency Request":

    st.markdown(
        '<p class="title">Emergency Organ Request</p>',
        unsafe_allow_html=True
    )

    emergency_name = st.text_input(
        "Patient Name"
    )

    emergency_organ = st.selectbox(
        "Needed Organ",
        ORGANS
    )

    emergency_hospital = st.selectbox(
        "Hospital",
        VALID_HOSPITALS
    )

    emergency_contact = st.text_input(
        "Emergency Contact Number"
    )

    if st.button("Send Emergency Alert"):

        if valid_phone(emergency_contact):

            st.success(
                "Emergency Alert Sent 🚨"
            )

        else:

            st.error(
                "Invalid Contact Number"
            )

# ---------------- ADMIN DASHBOARD ---------------- #

elif page == "Admin Dashboard":

    st.markdown(
        '<p class="title">Admin Dashboard</p>',
        unsafe_allow_html=True
    )

    st.subheader("Registered Donors")

    donor_df = pd.DataFrame(
        st.session_state.donors
    )

    st.dataframe(donor_df)

    st.subheader("Registered Patients")

    patient_df = pd.DataFrame(
        st.session_state.patients
    )

    st.dataframe(patient_df)

# ---------------- AWARENESS PAGE ---------------- #

elif page == "Awareness":

    st.markdown(
        '<p class="title">Organ Donation Awareness</p>',
        unsafe_allow_html=True
    )

    st.info("""
    One organ donor can save up to 8 lives ❤️
    """)

    st.write("""
    ✔ Organ donation gives a second life  
    ✔ Helps critical patients survive  
    ✔ Encourages humanity and kindness  
    ✔ Creates medical support for society  
    """)

# ---------------- FAQ PAGE ---------------- #

elif page == "FAQ":

    st.markdown(
        '<p class="title">Frequently Asked Questions</p>',
        unsafe_allow_html=True
    )

    with st.expander("Who can donate organs?"):
        st.write(
            "Healthy individuals above 18 years."
        )

    with st.expander("Is organ donation safe?"):
        st.write(
            "Yes, hospitals follow strict rules."
        )

    with st.expander("Can one donor save lives?"):
        st.write(
            "Yes, one donor can save multiple lives."
        )

# ---------------- ABOUT PAGE ---------------- #

elif page == "About":

    st.markdown(
        '<p class="title">About Donate Life AI</p>',
        unsafe_allow_html=True
    )

    st.write("""
    Donate Life AI is an advanced
    AI-powered organ donation system.

    Features Included:
    
    ✔ Donor Registration  
    ✔ Patient Registration  
    ✔ AI Match System  
    ✔ Emergency Requests  
    ✔ Admin Dashboard  
    ✔ OTP Login  
    ✔ Data Validation  
    ✔ Awareness Section  
    ✔ FAQ Section  
    """)

    st.success(
        "Made With ❤️ Using Streamlit"
    )
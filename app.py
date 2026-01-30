import streamlit as st
import numpy as np
import pandas as pd
import pickle
import plotly.graph_objects as go

# ================== TEXT ==================
TEXT = {

    # ================== ENGLISH ==================
    "English": {
        "lang_label": "🌐 Select Language",
        "title": "Loan Approval Prediction",
        "predict": "Predict",
        "approved": "Loan Approved",
        "rejected": "Loan Not Approved",
        "advisor": "AI Loan Advisor",
        "risk": "Risk Assessment",
        "low": "LOW RISK Applicant",
        "medium": "MEDIUM RISK Applicant",
        "high": "HIGH RISK Applicant",
        "smart": "Smart Loan Suggestion",
        "what_if": "AI What-If Simulation",
        "explain": "Decision Explanation",
        "inc_income": "Increase Income (%)",
        "emi": "Estimated Monthly EMI",
        "emi_ratio": "EMI-to-Income Ratio",
        "safe_loan": "Safe loan amount",
        "credit_weak": "Credit history is weak.",
        "emi_ok": "EMI is affordable.",
        "emi_bad": "EMI is too high.",
        "income_ok": "Income sufficient",
        "income_bad": "Income insufficient",

        "gender": "Gender",
        "married": "Married",
        "education": "Education",
        "self_emp": "Self Employed",
        "property": "Property Area",
        "credit": "Credit History",
        "app_income": "Applicant Income",
        "co_income": "Coapplicant Income",
        "loan_amt": "Loan Amount",
        "loan_term": "Loan Amount Term (months)"
    },
# ================== BHOJPURI ==================
"Bhojpuri": {
        "lang_label": "🌐 भाषा चुनीं",
        "title": "लोन मंजूरी अनुमान",
        "predict": "जाँच करीं",
        "approved": "लोन मंजूर हो गइल",
        "rejected": "लोन मंजूर ना भइल",
        "advisor": "AI लोन सलाहकार",
        "risk": "जोखिम जाँच",
        "low": "कम जोखिम वाला आवेदक",
        "medium": "मध्यम जोखिम वाला आवेदक",
        "high": "ज्यादा जोखिम वाला आवेदक",
        "smart": "समझदार लोन सुझाव",
        "what_if": "अगर-अइसन हो त",
        "explain": "फैसला के कारण",
        "inc_income": "कमाई बढ़ाईं (%)",
        "emi": "अनुमानित EMI",
        "emi_ratio": "EMI बनाम कमाई अनुपात",
        "safe_loan": "सुरक्षित लोन राशि",
        "credit_weak": "क्रेडिट हिस्ट्री कमजोर बा",
        "emi_bad": "EMI कमाई से बहुत जादा बा",
        "income_bad": "कमाई पूरा ना पड़त बा",

        "gender": "लिंग",
        "married": "शादीशुदा",
        "education": "पढ़ाई",
        "self_emp": "खुद के रोजगार",
        "property": "प्रॉपर्टी इलाका",
        "credit": "क्रेडिट हिस्ट्री",
        "app_income": "आवेदक के कमाई",
        "co_income": "सह-आवेदक के कमाई",
        "loan_amt": "लोन राशि",
        "loan_term": "लोन अवधि (महीना)"
    },
    # ================== MARATHI ==================
    "Marathi": {
        "lang_label": "🌐 भाषा निवडा",
        "title": "कर्ज मंजुरी अंदाज",
        "predict": "तपासा",
        "approved": "कर्ज मंजूर",
        "rejected": "कर्ज नाकारले",
        "advisor": "AI कर्ज सल्लागार",
        "risk": "जोखीम मूल्यांकन",
        "low": "कमी जोखीम अर्जदार",
        "medium": "मध्यम जोखीम अर्जदार",
        "high": "उच्च जोखीम अर्जदार",
        "smart": "स्मार्ट कर्ज सूचना",
        "what_if": "AI काय-झाले-तर",
        "explain": "निर्णय स्पष्टीकरण",
        "inc_income": "उत्पन्न वाढ (%)",
        "emi": "अंदाजे EMI",
        "emi_ratio": "EMI-उत्पन्न गुणोत्तर",
        "safe_loan": "सुरक्षित कर्ज रक्कम",
        "credit_weak": "क्रेडिट इतिहास कमजोर आहे.",
        "emi_ok": "EMI परवडणारी आहे.",
        "emi_bad": "EMI जास्त आहे.",
        "income_ok": "उत्पन्न पुरेसे आहे",
        "income_bad": "उत्पन्न अपुरे आहे",

        "gender": "लिंग",
        "married": "विवाहित",
        "education": "शिक्षण",
        "self_emp": "स्वयंरोजगार",
        "property": "मालमत्ता क्षेत्र",
        "credit": "क्रेडिट इतिहास",
        "app_income": "अर्जदाराचे उत्पन्न",
        "co_income": "सह-अर्जदाराचे उत्पन्न",
        "loan_amt": "कर्ज रक्कम",
        "loan_term": "कर्ज कालावधी (महिने)"
    },

    # ================== GUJARATI ==================
    "Gujarati": {
        "lang_label": "🌐 ભાષા પસંદ કરો",
        "title": "લોન મંજૂરી અનુમાન",
        "predict": "ચકાસો",
        "approved": "લોન મંજૂર",
        "rejected": "લોન નકારાયેલ",
        "advisor": "AI લોન સલાહકાર",
        "risk": "જોખમ મૂલ્યાંકન",
        "low": "ઓછું જોખમ અરજદાર",
        "medium": "મધ્યમ જોખમ અરજદાર",
        "high": "ઉચ્ચ જોખમ અરજદાર",
        "smart": "સ્માર્ટ લોન સૂચન",
        "what_if": "AI શું-જો",
        "explain": "નિર્ણય સ્પષ્ટીકરણ",
        "inc_income": "આવક વધારો (%)",
        "emi": "અંદાજિત EMI",
        "emi_ratio": "EMI-આવક અનુપાત",
        "safe_loan": "સુરક્ષિત લોન રકમ",
        "credit_weak": "ક્રેડિટ ઇતિહાસ નબળો છે.",
        "emi_ok": "EMI યોગ્ય છે.",
        "emi_bad": "EMI વધારે છે.",
        "income_ok": "આવક પૂરતી છે",
        "income_bad": "આવક અપૂરતી છે",

        "gender": "લિંગ",
        "married": "વિવાહિત",
        "education": "શિક્ષણ",
        "self_emp": "સ્વરોજગાર",
        "property": "મિલકત વિસ્તાર",
        "credit": "ક્રેડિટ ઇતિહાસ",
        "app_income": "અરજદારની આવક",
        "co_income": "સહ-અરજદારની આવક",
        "loan_amt": "લોન રકમ",
        "loan_term": "લોન સમયગાળો (મહિના)"
    },

    # ================== BENGALI ==================
    "Bengali": {
        "lang_label": "🌐 ভাষা নির্বাচন করুন",
        "title": "ঋণ অনুমোদন পূর্বাভাস",
        "predict": "পরীক্ষা করুন",
        "approved": "ঋণ অনুমোদিত",
        "rejected": "ঋণ বাতিল",
        "advisor": "AI ঋণ পরামর্শক",
        "risk": "ঝুঁকি মূল্যায়ন",
        "low": "কম ঝুঁকির আবেদনকারী",
        "medium": "মাঝারি ঝুঁকির আবেদনকারী",
        "high": "উচ্চ ঝুঁকির আবেদনকারী",
        "smart": "স্মার্ট ঋণ পরামর্শ",
        "what_if": "AI যদি-হয়",
        "explain": "সিদ্ধান্ত ব্যাখ্যা",
        "inc_income": "আয় বৃদ্ধি (%)",
        "emi": "আনুমানিক EMI",
        "emi_ratio": "EMI-আয় অনুপাত",
        "safe_loan": "নিরাপদ ঋণের পরিমাণ",
        "credit_weak": "ক্রেডিট ইতিহাস দুর্বল।",
        "emi_ok": "EMI সহনীয়।",
        "emi_bad": "EMI বেশি।",
        "income_ok": "আয় যথেষ্ট",
        "income_bad": "আয় অপর্যাপ্ত",

        "gender": "লিঙ্গ",
        "married": "বিবাহিত",
        "education": "শিক্ষা",
        "self_emp": "স্বনিযুক্ত",
        "property": "সম্পত্তি এলাকা",
        "credit": "ক্রেডিট ইতিহাস",
        "app_income": "আবেদনকারীর আয়",
        "co_income": "সহ-আবেদনকারীর আয়",
        "loan_amt": "ঋণের পরিমাণ",
        "loan_term": "ঋণের মেয়াদ (মাস)"
    },
    # ================== TAMIL ==================
    "Tamil": {
        "lang_label": "🌐 மொழியை தேர்வு செய்யவும்",
        "title": "கடன் அனுமதி கணிப்பு",
        "predict": "சரிபார்க்கவும்",
        "approved": "கடன் அனுமதிக்கப்பட்டது",
        "rejected": "கடன் மறுக்கப்பட்டது",
        "advisor": "AI கடன் ஆலோசகர்",
        "risk": "ஆபத்து மதிப்பீடு",
        "low": "குறைந்த ஆபத்து விண்ணப்பதாரர்",
        "medium": "மிதமான ஆபத்து விண்ணப்பதாரர்",
        "high": "உயர் ஆபத்து விண்ணப்பதாரர்",
        "smart": "ஸ்மார்ட் கடன் பரிந்துரை",
        "what_if": "AI என்ன-ஆனால்",
        "explain": "முடிவு விளக்கம்",
        "inc_income": "வருமான உயர்வு (%)",
        "emi": "மதிப்பிடப்பட்ட EMI",
        "emi_ratio": "EMI-வருமான விகிதம்",
        "safe_loan": "பாதுகாப்பான கடன் தொகை",
        "credit_weak": "கடன் வரலாறு பலவீனமாக உள்ளது.",
        "emi_ok": "EMI ஏற்றதாக உள்ளது.",
        "emi_bad": "EMI அதிகமாக உள்ளது.",
        "income_ok": "வருமானம் போதுமானது",
        "income_bad": "வருமானம் போதாது",

        "gender": "பாலினம்",
        "married": "திருமணமானவர்",
        "education": "கல்வி",
        "self_emp": "சுயதொழில்",
        "property": "சொத்து பகுதி",
        "credit": "கடன் வரலாறு",
        "app_income": "விண்ணப்பதாரரின் வருமானம்",
        "co_income": "இணை விண்ணப்பதாரரின் வருமானம்",
        "loan_amt": "கடன் தொகை",
        "loan_term": "கடன் காலம் (மாதங்கள்)"
    }
}


language = st.selectbox(TEXT["English"]["lang_label"], list(TEXT.keys()))
T = lambda k: TEXT[language][k]

# ================== MODEL ==================
try:
    with open("loan_approval_model.pkl", "rb") as f:
        model = pickle.load(f)
except Exception as e:
    st.error("❌ Model loading failed. Please check scikit-learn version compatibility.")
    st.stop()
st.title(T("title"))

# ================== INPUTS ==================
Gender = st.selectbox(T("gender"), ["Male", "Female"])
Married = st.selectbox(T("married"), ["Yes", "No"])
Education = st.selectbox(T("education"), ["Graduate", "Not Graduate"])
Self_Employed = st.selectbox(T("self_emp"), ["Yes", "No"])
Property_Area = st.selectbox(T("property"), ["Urban", "Semiurban", "Rural"])
Credit_History = st.selectbox(T("credit"), [1.0, 0.0])

ApplicantIncome = st.number_input(T("app_income"), min_value=0)
CoapplicantIncome = st.number_input(T("co_income"), min_value=0)
LoanAmount = st.number_input(T("loan_amt"), min_value=0)
Loan_Amount_Term = st.number_input(T("loan_term"), min_value=0)

income = ApplicantIncome + CoapplicantIncome
monthly_income = income / 12 if income > 0 else 0

# ================== PREDICT ==================
if st.button(T("predict")):

    df = pd.DataFrame([{
        "Gender": Gender,
        "Married": Married,
        "Education": Education,
        "Self_Employed": Self_Employed,
        "Property_Area": Property_Area,
        "Credit_History": Credit_History,
        "Log_Income": np.log1p(income),
        "LoanAmount": LoanAmount,
        "Loan_Amount_Term": Loan_Amount_Term
    }])

    proba = model.predict_proba(df)[0][1]

    # ---------- EMI ----------
    interest = 9.0
    r = interest / (12 * 100)
    emi = (LoanAmount * r * (1+r)**Loan_Amount_Term)/((1+r)**Loan_Amount_Term - 1) if Loan_Amount_Term>0 else 0
    emi_ratio = emi / monthly_income if monthly_income>0 else 1

    # ---------- FINAL BANK DECISION ----------
    reasons = []

    if Credit_History != 1.0:
        reasons.append(T("credit_weak"))
    if emi_ratio > 0.40:
        reasons.append(T("emi_bad"))
    if monthly_income <= 0:
        reasons.append(T("income_bad"))

    approved = len(reasons) == 0

    if approved:
        st.success(T("approved"))
    else:
        st.error(T("rejected"))

    # ---------- GAUGE (MODEL CONFIDENCE) ----------
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=proba * 100,
        title={"text": "Model Confidence (%)"},
        number={"suffix": "%"},
        gauge={"axis": {"range": [0, 100]}}
    ))
    st.plotly_chart(fig, use_container_width=True)

    # ---------- EMI INFO ----------
    st.write(f"💰 {T('emi')}: ₹{emi:,.2f}")
    st.write(f"📊 {T('emi_ratio')}: {emi_ratio:.2f}")

    # ---------- ADVISOR ----------
    st.markdown(f"### 🤖 {T('advisor')}")
    if approved:
        st.info("Profile and affordability both are acceptable")
    else:
        for r in reasons:
            st.warning(r)

        if proba >= 0.70:
            st.info("Your profile is strong, but affordability is the issue")

    # ---------- RISK ----------
    st.markdown(f"### ⚠️ {T('risk')}")
    if proba >= 0.70:
        st.success(T("low"))
    elif proba >= 0.50:
        st.warning(T("medium"))
    else:
        st.error(T("high"))

    # ---------- SMART LOAN ----------
    st.markdown(f"### 💡 {T('smart')}")
    st.info(f"{T('safe_loan')}: ₹{int(monthly_income * 20)}")

    # ---------- WHAT-IF ----------
    st.markdown(f"### 🧪 {T('what_if')}")
    boost = st.slider(T("inc_income"), 0, 50, 0)
    sim_income = income * (1 + boost / 100)
    sim_monthly = sim_income / 12 if sim_income > 0 else 0
    sim_ratio = emi / sim_monthly if sim_monthly > 0 else 1

    if sim_ratio <= 0.40:
        st.success("With increased income, EMI becomes affordable")
    else:
        st.info("Even after income increase, EMI is high")

    # ---------- EXPLANATION ----------
    st.markdown(f"### 🔍 {T('explain')}")
    st.write(f"• Credit History: {Credit_History}")
    st.write(f"• Model Probability: {proba:.2f}")
    st.write(f"• EMI Ratio: {emi_ratio:.2f}")
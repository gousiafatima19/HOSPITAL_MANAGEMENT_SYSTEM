from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import google.generativeai as genai  
from django.conf import settings
from doctors.models import Doctor
from patients.models import Patient
import markdown_it
 
 
# Create your views here.
@login_required
def dashboard_home(request):
    return render(request, "dashboard_home.html")
 
 
@login_required
def dashboard_hms_ai(request):
    if request.method == 'POST':
        user_query = request.POST.get('query')
 
       
        genai.configure(api_key=settings.GEMINI_API_KEY)
 
       
        doctors = Doctor.objects.all()
        patients = Patient.objects.all()
 
        doctors = list(doctors.values())
        patients = list(patients.values())
 
   
        final_query = f'''
        You are the AI chatbot inside a website called CuraHMS.
        Your responsibility is to answer questions ONLY about CURAHMS data.
        If question is outside this, say: "I can only answer HMS-related queries."
 
        Doctors data:
        {doctors}
 
        Patients data:
        {patients}
 
        User question:
        {user_query}
        '''
 
        try:
           
            model = genai.GenerativeModel("gemini-2.5-flash")
 
            response = model.generate_content(final_query)
 
            md = markdown_it.MarkdownIt()
 
 
            answer = md.render(response.text if hasattr(response, "text") else "No response generated.")
 
        except Exception as e:
            answer = f"<p>Error: {str(e)}</p>"
 
        return render(request, "dashboard_hms_ai.html", {
            'answer': answer
        })
 
    return render(request, "dashboard_hms_ai.html")
 





 

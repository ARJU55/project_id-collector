import io
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import ProjectDetails
from  reportlab.pdfgen import canvas   

class GeneratePDFView(View):
    def get(self, request, project_id):
        project_details = get_object_or_404(ProjectDetails, id=project_id)
# Create a file-like buffer to receive PDF data.
        buffer = io.BytesIO()

        # Create the PDF object, using the buffer as its "file."
        p = canvas.Canvas(buffer)

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.syllabus
        p.setFont("Helvetica", 18)
        p.drawString(100, 750, f"{project_details.Title_of_theproject}")
        p.drawString(100, 730, f"{project_details.Description}")
        p.setFont("Helvetica", 12)
        p.drawString(100, 710, f"{project_details.course}")
        p.drawString(100, 690, f"{project_details.syllabus}")

        # Close the PDF object cleanly, and save it to the buffer.
        p.showPage()
        p.save()

        # Get the value of the BytesIO buffer and write it to the response.
        pdf = buffer.getvalue()
        buffer.close()
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{project_details.Title_of_theproject}.pdf"'
        return response



class ShowProjectList(View):
    def get(self, request):
        projects = ProjectDetails.objects.all()
        return render(request, 'project_list.html', {'projects': projects})  



class ViewPdf(View):
    def get(self, request, project_id):
        project_deatails = get_object_or_404(ProjectDetails, id=project_id) 
        print(project_deatails)      
        return render(request, 'project_details.html', {'projects': project_deatails})
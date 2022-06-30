from flask import Flask,jsonify,request
from bs4 import BeautifulSoup
import pandas as pd
import requests
app = Flask(__name__)

def todo():
    #url = 'https://resultados.as.com/resultados/futbol/primera/clasificacion/'
    url = 'https://resultados.as.com/resultados/futbol/primera/2021_2022/clasificacion/'

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    equipo = soup.find_all('span', class_= 'nombre-equipo')#listado de equipos
    NomEqui = list()
    for i in equipo:
        NomEqui.append(i.text)
    Puntos = soup.find_all('td', class_= 'destacado') #puntos de equipo
    Pts = list()
    for i in Puntos:
        Pts.append(i.text)

    todo = {}
    h=0
    for i in range(len(NomEqui)):
        todo[NomEqui[i]]=[]
    for i in range(len(NomEqui)):
        todo[NomEqui[i]].append(Pts[i])

    return todo

@app.route('/futbol',methods=["GET"])
def futbol():
    todos = todo()

    html = '<head>'
    html += '   <meta charset="utf-8">'
    html += '   <meta http-equiv="X-UA-Compatible" content="IE=edge">'
    html += '   <title>ChartJS</title>'
    html += '   <meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport">'
    html += '   <link rel="stylesheet" href="https://adminlte.io/themes/AdminLTE/bower_components/bootstrap/dist/css/bootstrap.min.css">'
    html += '   <link rel="stylesheet" href="https://adminlte.io/themes/AdminLTE/bower_components/font-awesome/css/font-awesome.min.css">'
    html += '   <link rel="stylesheet" href="https://adminlte.io/themes/AdminLTE/bower_components/Ionicons/css/ionicons.min.css">'
    html += '   <link rel="stylesheet" href="https://adminlte.io/themes/AdminLTE/dist/css/AdminLTE.min.css">'
    html += '   <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,600,700,300italic,400italic,600italic">'
    html += '</head>'
    html += '<body class="hold-transition skin-blue sidebar-mini">'
    html += '   <div class="wrapper">'
    html += '      <section class="content">'
    html += '           <div class="row">'
    html += '               <div class="col-md-6">'
    html += '                   <div class="box box-danger">'
    html += '                       <div class="box-header with-border">'
    html += '                           <h3 class="box-title">Total</h3>'
    html += '                       </div>'
    html += '                   <div class="box-body">'
    html += '                       <canvas id="pieChart0" style="height:250px"></canvas>'
    html += '                   </div>'
    html += '               </div></div>'
    html += '               <div class="col-md-6">'
    html += '                   <div class="box box-danger">'
    html += '                       <div class="box-header with-border">'
    html += '                           <h3 class="box-title">En casa</h3>'
    html += '                       </div>'
    html += '                   <div class="box-body">'
    html += '                       <canvas id="pieChart1" style="height:250px"></canvas>'
    html += '                   </div>'
    html += '               </div></div>'
    html += '               <div class="col-md-6">'
    html += '                   <div class="box box-danger">'
    html += '                       <div class="box-header with-border">'
    html += '                           <h3 class="box-title">Visitante</h3>'
    html += '                       </div>'
    html += '                   <div class="box-body">'
    html += '                       <canvas id="pieChart2" style="height:250px"></canvas>'
    html += '                   </div>'
    html += '               </div></div>'

    html += '               <div class="col-md-6">'
    html += '                   <div class="box box-success">'
    html += '                       <div class="box-header with-border">'
    html += '                           <h3 class="box-title">Todo</h3>'
    html += '                       </div>'
    html += '                       <div class="box-body">'
    html += '                           <div class="chart">'
    html += '                               <canvas id="barChart" style="height:230px"></canvas>'
    html += '                           </div>'
    html += '                       </div>'
    html += '                   </div>'
    html += '               </div>'
    html += '           </div>'
    html += '       </section>'
    html += '   </div>'


    html += '   <script src="https://adminlte.io/themes/AdminLTE/bower_components/jquery/dist/jquery.min.js"></script>'
    html += '   <script src="https://adminlte.io/themes/AdminLTE/bower_components/bootstrap/dist/js/bootstrap.min.js"></script>'
    html += '   <script src="https://adminlte.io/themes/AdminLTE/bower_components/chart.js/Chart.js"></script>'
    html += '   <script>'
    html += '       function generarLetra() {'
    html += '           var letras = ["a", "b", "c", "d", "e", "f", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];'
    html += '           var numero = (Math.random() * 15).toFixed(0);'
    html += '           return letras[numero];'
    html += '       }'

    html += '       function colorHEX() {'
    html += '           var coolor = "";'
    html += '           for (var i = 0; i < 6; i++) {'
    html += '               coolor = coolor + generarLetra();'
    html += '           }'
    html += '           return "#" + coolor;'
    html += '       }'


    html += '       var pieChartCanvas0 = $("#pieChart0").get(0).getContext("2d");'
    html += '       var pieChart0 = new Chart(pieChartCanvas0);'
    html += '       var pieChartCanvas1 = $("#pieChart1").get(0).getContext("2d");'
    html += '       var pieChart1 = new Chart(pieChartCanvas1);'
    html += '       var pieChartCanvas2 = $("#pieChart2").get(0).getContext("2d");'
    html += '       var pieChart2 = new Chart(pieChartCanvas2);'

    html += '       var PieData0 = ['
    for i in todos:
        html += '{value: '+todos[i][0]+', color: colorHEX(),highlight: colorHEX(),label: "'+i+'"},'
    html += '       ];'
    html += '       var PieData1 = ['
    for i in todos:
        html += '{value: '+todos[i][1]+', color: colorHEX(),highlight: colorHEX(),label: "'+i+'"},'
    html += '       ];'
    html += '       var PieData2 = ['
    for i in todos:
        html += '{value: '+todos[i][2]+', color: colorHEX(),highlight: colorHEX(),label: "'+i+'"},'
    html += '       ];'

    html += '       var pieOptions = {'
    html += '           segmentShowStroke: true,'
    html += '           segmentStrokeColor: "#fff",'
    html += '           segmentStrokeWidth: 2,'
    html += '           percentageInnerCutout: 50, '
    html += '           animationSteps: 100,'
    html += '           animationEasing: "easeOutBounce",'
    html += '           animateRotate: true,'
    html += '           animateScale: false,'
    html += '           responsive: true,'
    html += '           maintainAspectRatio: true };'
    html += '       pieChart0.Doughnut(PieData0, pieOptions);'
    html += '       pieChart1.Doughnut(PieData1, pieOptions);'
    html += '       pieChart2.Doughnut(PieData2, pieOptions);'

    
    nombres = []
    p1 = []
    p2 = []
    p3 = []
    for i in todos:
        nombres.append(i)
        p1.append(todos[i][0])
        p2.append(todos[i][1])
        p3.append(todos[i][2])


    html += '       var fill_1 = colorHEX();'
    html += '       var stroke_1 = colorHEX();'
    html += '       var point_1 = colorHEX();'
    html += '       var areaChartData = {'
    html += '               labels: '+str(nombres)+','
    html += '               datasets: [{'
    html += '                       label: "Total",'
    html += '                       fillColor: fill_1,'
    html += '                       strokeColor: fill_1,'
    html += '                       pointColor: fill_1,'
    html += '                       pointStrokeColor: fill_1,'
    html += '                       pointHighlightFill: "#fff",'
    html += '                       pointHighlightStroke: fill_1,'
    html += '                       data: '+str(p1)
    html += '                   },'
    html += '                   {'
    html += '                       label: "En Casa",'
    html += '                       fillColor: stroke_1,'
    html += '                       strokeColor: stroke_1,'
    html += '                       pointColor: stroke_1,'
    html += '                       pointStrokeColor: stroke_1,'
    html += '                       pointHighlightFill: "#fff",'
    html += '                       pointHighlightStroke: stroke_1,'
    html += '                       data: '+str(p2)
    html += '                   },'
    html += '                   {'
    html += '                       label: "Visitante",'
    html += '                       fillColor: point_1,'
    html += '                       strokeColor: point_1,'
    html += '                       pointColor: point_1,'
    html += '                       pointStrokeColor: point_1,'
    html += '                       pointHighlightFill: "#fff",'
    html += '                       pointHighlightStroke: point_1,'
    html += '                       data: '+str(p3)
    html += '                   },'
    html += '               ]'
    html += '           };'


    html += '           var barChartCanvas = $("#barChart").get(0).getContext("2d");'
    html += '           var barChart = new Chart(barChartCanvas);'
    
    html += '           var barChartData = areaChartData;'
    html += '           var barChartOptions = {'
    html += '                   scaleBeginAtZero: true,'
    html += '                   scaleShowGridLines: true,'
    html += '                   scaleGridLineColor: "rgba(0,0,0,.05)",'
    html += '                   scaleGridLineWidth: 1,'
    html += '                   scaleShowHorizontalLines: true,'
    html += '                   scaleShowVerticalLines: true,'
    html += '                   barShowStroke: true,'
    html += '                   barStrokeWidth: 2,'
    html += '                   barValueSpacing: 5,'
    html += '                   barDatasetSpacing: 1,'
    html += '                   responsive: true,'
    html += '                   maintainAspectRatio: true'
    html += '            };'

    html += '            barChartOptions.datasetFill = false;'
    html += '            barChart.Bar(barChartData, barChartOptions);'

    html += '   </script>'

    return html



@app.route('/json',methods=["GET"])
def json():
    todos2 = todo()
    return jsonify(todos2) 


@app.route('/html',methods=["GET"])
def html():
    todos1 = todo()
    h=0
    html = "<table border='1'>"
    html += "   <tr>"
    html += "     <th>Equipo</th>"
    html += "     <th>Total</th>"
    html += "     <th>En casa</th>"
    html += "     <th>Visita</th>"
    html += "   </tr>"
    html += "   <tbody>"
    for i in todos1:
        html += "<tr>"
        html += "  <td>"+i+"</td>"
        html += "  <td>"+todos1[i][0]+"</td>"
        html += "  <td>"+todos1[i][1]+"</td>"
        html += "  <td>"+todos1[i][2]+"</td>"
        html += "</tr>"

    html += "    </tbody>"
    html += "</table>" 
    #return jsonify(todo) 
    return html 

if __name__=="__main__":
    app.run(host="0.0.0.0",port=80)
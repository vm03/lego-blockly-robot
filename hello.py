#!/usr/bin/python3

import cgi, cgitb, base64, time

def InitHW():
    gpios = ["38", "39", "41", "42"]
    pwms = ["0", "2"]
    for x in gpios:
        out_file = open('/sys/class/gpio/export', 'w')
        out_file.write(x)
        out_file.close()
        out_file = open('/sys/class/gpio/gpio%s/direction' % (x), 'w')
        out_file.write("out")
        out_file.close()
        out_file = open('/sys/class/gpio/gpio%s/value' % (x), 'w')
        out_file.write("0")
        out_file.close()
    for x in pwms:
        out_file = open('/sys/class/pwm/pwmchip0/export', 'w')
        out_file.write(x)
        out_file.close()
        out_file = open('/sys/class/pwm/pwmchip0/pwm%s/period' % (x), 'w')
        out_file.write("100000")
        out_file.close()
        out_file = open('/sys/class/pwm/pwmchip0/pwm%s/duty_cycle' % (x), 'w')
        out_file.write("100000")
        out_file.close()
        out_file = open('/sys/class/pwm/pwmchip0/pwm%s/enable' % (x), 'w')                     
        out_file.write("0")
        out_file.close()

def StopMotor():
    gpios = ["38", "39", "41", "42"]                                          
    pwms = ["0", "2"]                                                         

    for x in gpios:                                                           
        out_file = open('/sys/class/gpio/gpio%s/value' % (x), 'w')
        out_file.write("1")                                                   
        out_file.close()                                                      
    time.sleep(1)                                                           
    for x in gpios:                                                           
        out_file = open('/sys/class/gpio/gpio%s/value' % (x), 'w')        
        out_file.write("0")                                                   
        out_file.close()                                                      

    for x in pwms:                                                            
        out_file = open('/sys/class/pwm/pwmchip0/pwm%s/enable' % (x), 'w')
        out_file.write("0")                                                   
        out_file.close()                                                      

def SetSpeed(speed):
    pwms = ["0", "2"]
    for x in pwms:
        out_file = open('/sys/class/pwm/pwmchip0/pwm%s/duty_cycle' % (x), 'w')
        out_file.write(str(speed)+'0000')
        out_file.close()
        out_file = open('/sys/class/pwm/pwmchip0/pwm%s/enable' % (x), 'w')        
        out_file.write("1")                                                   
        out_file.close()                                                      

def SetMotor(motor, sec, direction):
    if (motor == 'both'):
        if (direction == 'forward'):
            gpios = ["42", "39"]
        if (direction == 'backward'):
            gpios = ["41", "38"]
    if (motor == 'left'):
        if (direction == 'forward'):                                          
            gpios = ["39"]                                              
        if (direction == 'backward'):                                         
            gpios = ["41"]                                              
    if (motor == 'right'):
        if (direction == 'forward'):                                          
            gpios = ["42"]                                              
        if (direction == 'backward'):                                         
            gpios = ["38"]                                              
    for x in gpios:                                                           
        out_file = open('/sys/class/gpio/gpio%s/value' % (x), 'w')
        out_file.write("1")                                                   
        out_file.close()                                                      
    time.sleep(sec)
    for x in gpios:
        out_file = open('/sys/class/gpio/gpio%s/value' % (x), 'w')                                                           
        out_file.write("0")                                                   
        out_file.close()                                                      


form = cgi.FieldStorage() 
data64 = form.getvalue('data')

code = base64.b64decode(data64).decode("utf-8", "ignore")

#InitHW()

#code = 'StopMotor()'

print ("Content-type:text/html\r\n\r\n")
#print '<html>'
#print '<head>'
#print '<title>Py Hello!</title>'
#print '</head>'
#print '<body>'
print ('<h3>Running code:</h3>')
print ('<pre>')
print (code)
print ('</pre>')
print ('<pre>')
exec(code)
print ('</pre>')
print ('<h3>Done</h3>')

#print '</body>'
#print '</html>'


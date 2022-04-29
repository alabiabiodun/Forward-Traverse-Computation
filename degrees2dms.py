def deg2dms(dd):
    if dd > 0:
        deg = int(dd)
        min = int((dd - deg) * 60)
        sec = round((((dd - deg) * 60) - min)*60, 0)
        #dt = str(deg) + str('°') + ' ' + str(min) + str('’') + ' ' + str(sec) + str('"')
        if len(str(int(deg))) == 1 and len(str(int(min))) == 1 and len(str(int(sec))) == 1:
            return '{} {} {}'.format('0'+str(deg)+'°','0'+str(min)+"'",'0'+str('%0.0f'%sec)+'"')
            
        elif len(str(int(deg))) == 2 and len(str(int(min))) == 1 and len(str(int(sec))) == 1:
            return '{} {} {}'.format(str(deg)+'°','0'+str(min)+"'",'0'+str('%0.0f'%sec)+'"')
        
        elif len(str(int(deg))) == 1 and len(str(int(min))) == 2 and len(str(int(sec))) == 2:
            return '{} {} {}'.format('0'+str(deg)+'°',str(min)+"'",str('%0.0f'%sec)+'"')
        
        elif len(str(int(deg))) == 2 and len(str(int(min))) == 1 and len(str(int(sec))) == 2:
            return '{} {} {}'.format(str(deg)+'°','0'+str(min)+"'",str('%0.0f'%sec)+'"')
        
        elif len(str(int(deg))) == 2 and len(str(int(min))) == 2 and len(str(int(sec))) == 1:
            return '{} {} {}'.format(str(deg)+'°',str(min)+"'",'0'+str('%0.0f'%sec)+'"')
        
        elif len(str(int(deg))) == 1 and len(str(int(min))) == 1 and len(str(int(sec))) == 2:
            return '{} {} {}'.format('0'+str(deg)+'°','0'+str(min)+"'",str('%0.0f'%sec)+'"')
        
        elif len(str(int(deg))) == 1 and len(str(int(min))) == 2 and len(str(int(sec))) == 1:
            return '{} {} {}'.format('0'+str(deg)+'°',str(min)+"'",'0'+str('%0.0f'%sec)+'"')
        
        
        elif len(str(int(deg))) == 3 and len(str(int(min))) == 1 and len(str(int(sec))) == 1:
            return '{} {} {}'.format(str(deg)+'°','0'+str(min)+"'",'0'+str('%0.0f'%sec)+'"')
            
               
        elif len(str(int(deg))) == 3 and len(str(int(min))) == 1 and len(str(int(sec))) == 2:
            return '{} {} {}'.format(str(deg)+'°','0'+str(min)+"'",str('%0.0f'%sec)+'"')
        
        elif len(str(int(deg))) == 3 and len(str(int(min))) == 2 and len(str(int(sec))) == 1:
            return '{} {} {}'.format(str(deg)+'°',str(min)+"'",'0'+str('%0.0f'%sec)+'"')
        
        else:
            return '{} {} {}'.format(str(deg)+'°',str(min)+"'",str('%0.0f'%sec)+'"')
    
    elif  dd < 0:
        deg = abs(int(dd))
        min = int((abs(dd) - deg) * 60)
        sec = round((((abs(dd) - deg) * 60) - min)*60, 0)
        #dt = str(deg) + str('°') + ' ' + str(min) + str('’') + ' ' + str(sec) +  str('"')
    
        if len(str(int(deg))) == 1 and len(str(int(min))) == 1 and len(str(int(sec))) == 1:
            return '{} {} {}'.format('0'+str(deg)+'°','0'+str(min)+"'",'0'+str('%0.0f'%sec)+'"')
            
        elif len(str(int(deg))) == 2 and len(str(int(min))) == 1 and len(str(int(sec))) == 1:
            return '{} {} {}'.format(str(deg)+'°','0'+str(min)+"'",'0'+str('%0.0f'%sec)+'"')
        
        elif len(str(int(deg))) == 1 and len(str(int(min))) == 2 and len(str(int(sec))) == 2:
            return '{} {} {}'.format('0'+str(deg)+'°',str(min)+"'",str('%0.0f'%sec)+'"')
        
        elif len(str(int(deg))) == 2 and len(str(int(min))) == 1 and len(str(int(sec))) == 2:
            return '{} {} {}'.format(str(deg)+'°','0'+str(min)+"'",str('%0.0f'%sec)+'"')
        
        elif len(str(int(deg))) == 2 and len(str(int(min))) == 2 and len(str(int(sec))) == 1:
            return '{} {} {}'.format(str(deg)+'°',str(min)+"'",'0'+str('%0.0f'%sec)+'"')
        
        elif len(str(int(deg))) == 3 and len(str(int(min))) == 1 and len(str(int(sec))) == 1:
            return '{} {} {}'.format(str(deg)+'°','0'+str(min)+"'",'0'+str('%0.0f'%sec)+'"')
            
               
        elif len(str(int(deg))) == 3 and len(str(int(min))) == 1 and len(str(int(sec))) == 2:
            return '{} {} {}'.format(str(deg)+'°','0'+str(min)+"'",str('%0.0f'%sec)+'"')
        
        elif len(str(int(deg))) == 3 and len(str(int(min))) == 2 and len(str(int(sec))) == 1:
            return '{} {} {}'.format(str(deg)+'°',str(min)+"'",'0'+str('%0.0f'%sec)+'"')
        
        else:
            return '{} {} {}'.format(str(deg)+'°',str(min)+"'",str('%0.0f'%sec)+'"')  

    
    
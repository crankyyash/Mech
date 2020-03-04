x=1; #Element number
theta=0; #material orientation angle
t=0.000104; #thickness
i=5; #number of integration points
c=1; #compositelayup number
k=6630; #difference between your topmost and bottomost element number
def generate():
        seq=(str(theta),".");
        mod_theta="".join(seq);
        print("*Elset, elset=CompositeLayup-",c,"-1, generate",file=myfile);
        print("   ",x," ,",x+k,", 170",file=myfile);
        print("** Section: CompositeLayup-",c,"-1",file=myfile);
        print("*Shell Section,elset=CompositeLayup-",c,"-1, composite, layup=CompositeLayup-",c,file=myfile);
        print("",t,", ",i,", cylinder, ",mod_theta,", ply-1",file=myfile);
while x<171:
        myfile=open('composite.txt','a');
        if x==170:
                theta=90;
                generate();
                myfile.close();
                break;
        generate();
        x=x+1;
        theta=round(theta+float(90/170),2);
        c=c+1;
        myfile.close();

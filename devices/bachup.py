class rwpsettingViewset(viewsets.ModelViewSet):
	# define queryset
    print("hi ok ")
    queryset = rwp_setting.objects.all()
    print("queryset is",queryset)

    data=queryset.last()
    print("OLc",data.olc)
    data = {'olc':data.olc,'drc':data.drc,'spn':data.spn,'units_type':data.unit_type,'company_name':data.company_name,'component_name':data.componant_name}
    print('data is:',data)
    # dosome()
    print("Hi Satish")
    
    
	# specify serializer to be used
    serializer_class = rwpsettingSerializer

    def dispatch(self, request):
        print("ok satish new ONE")

        # response = requests.get('http://127.0.0.1:8000/topicapirwp_setting/')

        try:
                # print("HELLO in if:",response.json()[-1])
                did=0
                did="234"
                cmpname='rwp'
                mqtt_client.publish(f'wd/{did}/updset/{cmpname}',str("{'olc':payal.olc,'drc':rwp.vikas,'spn':rwp.spn}"))
        except:
            print("Error")
        

# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import *
authors = serializers.SerializerMethodField("get_author_serializer")
publisher = serializers.SerializerMethodField("get_publisher_serializer")
# # Create a model serializer
# class GeeksSerializer(serializers.HyperlinkedModelSerializer):
# 	# specify model and fields
# 	class Meta:
# 		model = GeeksModel
# 		fields = ('Topic',)


# class TopicSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = MyObject
# 		fields = ('__all__')
# class DeviceSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 			model = Decice_details
# 			fields = ('__all__')


# class NewDeviceSerializer(serializers.HyperlinkedModelSerializer):
# 	# specify model and fields
# 	class Meta:
# 		model = NewDecice_details
# 		fields = ('__all__')



class TopicSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = topics
		fields=('__all__')




# # Create a model serializer
# class GeeksSerializer(serializers.HyperlinkedModelSerializer):
# 	# specify model and fields
# 	class Meta:
# 		model = GeeksModel
# 		fields = ('Topic',)


# class TopicSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = MyObject
# 		fields = ('all')
# class DeviceSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 			model = Decice_details
# 			fields = ('all')


# class NewDeviceSerializer(serializers.HyperlinkedModelSerializer):
# 	# specify model and fields
# 	class Meta:
# 		model = NewDecice_details
# 		fields = ('all')

class YearlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = repo_yearly
		fields=['device_id','service','sum','avg','count']

class DeviceSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = device_info
		fields='__all__'

class KeySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = key_info
		fields='__all__'

class HourlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = repo_hourly
		fields='__all__'

class MonthlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = repo_monthly
		fields='__all__'

class DailySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = repo_daily
		fields='__all__'

class GraphSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = graph_info
		fields='__all__'

class RwpstateSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Rwp_state
		fields='__all__'
class rwpsettingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = rwp_setting
		
		print("hi am from serilization")
		fields=['olc','drc','spn','unit_type','company_name','componant_name']

		def get_author_serializer(self):
			# here write the logic to compute the value based on object
			print("hi ok satish 1")
			return 1

		def get_publisher_serializer(self):
			# here write the logic to compute the value based on object
			print("hi ok satish 1")
			return 2
	rss=Meta()
	rss.get_author_serializer()
	rss.get_publisher_serializer()
class hppstateSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = hpp_state
		fields='__all__'
class hppsettingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = hpp_setting
		fields='__all__'

class cndsettingSerializer(serializers.HyperlinkedModelSerializer):
	# new_field = serializers.CharField()
	class Meta:
		model = cnd_setting
		fields='__all__'

class tdssettingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tds_setting
		fields='__all__'
class FflowsensettingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = F_flowsen_setting
		fields='__all__'

class PflowsensettingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = P_flowsen_setting
		fields='__all__'
class panelsettingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = panel_setting
		fields='__all__'
class atmsettingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = atm_setting
		fields='__all__'
# class consensettingSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = consen_setting
# 		fields='__all__'
class tap1settingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tap1_setting
		fields='__all__'
class tap2settingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tap2_setting
		fields='__all__'
class tap3settingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tap3_setting
		fields='__all__'
class tap4settingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = tap4_setting
		fields='__all__'
class ampv1stateSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ampv1_state
		fields='__all__'
class ampv1settingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ampv1_setting
		fields='__all__'
class ampv2stateSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ampv2_state
		fields='__all__'
class ampv2settingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ampv2_setting
		fields='__all__'

		
# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import *

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
		model = cnd_tds_repo_yearly
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
		model = cnd_tds_repo_hourly
		fields='__all__'

class MonthlySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = cnd_tds_repo_monthly
		fields='__all__'

class DailySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = cnd_tds_repo_daily
		fields='__all__'

class GraphSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = graph_info
		fields='__all__'
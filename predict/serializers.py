from rest_framework import serializers

class PredictSerializer(serializers.Serializer):
    """
    A predict serializer
    """
    employee                        = serializers.DecimalField(max_digits=20, decimal_places=3)
    ownership                       = serializers.DecimalField(max_digits=20, decimal_places=3)
    credit_history                  = serializers.DecimalField(max_digits=20, decimal_places=3)
    sales                           = serializers.DecimalField(max_digits=20, decimal_places=3)
    credit                          = serializers.DecimalField(max_digits=20, decimal_places=3)
    turnover                        = serializers.DecimalField(max_digits=20, decimal_places=3)
    age_of_business                 = serializers.DecimalField(max_digits=20, decimal_places=3)
    fixed_asset_value               = serializers.DecimalField(max_digits=20, decimal_places=3)
    defaulted                       = serializers.DecimalField(max_digits=20, decimal_places=3)
    business_type                   = serializers.DecimalField(max_digits=20, decimal_places=3)
from ..models import *


class setupTestDB:
    @staticmethod
    def insert_test_data():
        max_time = 10
        col = Collection.objects.create(name='col1')
        lkup_key = str(col.pk)
        bs_key = col.name
        BossLookup.objects.create(lookup_key=lkup_key, boss_key=bs_key, collection_name=col.name)

        cf = CoordinateFrame.objects.create(name='cf1', description='cf1',
                                            x_start=0, x_stop=1000,
                                            y_start=0, y_stop=1000,
                                            z_start=0, z_stop=1000,
                                            x_voxel_size=4, y_voxel_size=4, z_voxel_size=4,
                                            time_step=1
                                            )

        # SETUP AN EXPERIMENT
        exp = Experiment.objects.create(name='exp1', collection=col, coord_frame=cf, num_hierarchy_levels=10,
                                        max_time_sample=max_time)
        lkup_key = str(col.pk) + '&' + str(exp.pk)
        bs_key = col.name + '&' + str(exp.name)
        BossLookup.objects.create(lookup_key=lkup_key, boss_key=bs_key, collection_name=col.name,
                                  experiment_name=exp.name)

        # SETUP A CHANNEL
        channel = ChannelLayer.objects.create(name='channel1', experiment=exp, is_channel=True, default_time_step=0,
                                              base_resolution=0, datatype='uint8')
        base_lkup_key = str(col.pk) + '&' + str(exp.pk) + '&' + str(channel.pk)
        base_bs_key = col.name + '&' + exp.name + '&' + channel.name
        BossLookup.objects.create(lookup_key=base_lkup_key, boss_key=base_bs_key,
                                  collection_name=col.name,
                                  experiment_name=exp.name,
                                  channel_layer_name=channel.name
                                  )
        for time in range(0, max_time + 1):
            lkup_key = base_lkup_key + '&' + str(time)
            bs_key = base_bs_key + '&' + str(time)
            BossLookup.objects.create(lookup_key=lkup_key, boss_key=bs_key,
                                      collection_name=col.name,
                                      experiment_name=exp.name,
                                      channel_layer_name=channel.name
                                      )

        # SETUP A LAYER
        layer = ChannelLayer.objects.create(name='layer1', experiment=exp, is_channel=False, default_time_step=0,
                                            base_resolution=0, datatype='uint8')
        base_lkup_key = str(col.pk) + '&' + str(exp.pk) + '&' + str(layer.pk)
        base_bs_key = col.name + '&' + exp.name + '&' + layer.name
        BossLookup.objects.create(lookup_key=base_lkup_key, boss_key=base_bs_key,
                                  collection_name=col.name,
                                  experiment_name=exp.name,
                                  channel_layer_name=channel.name
                                  )
        for time in range(0, max_time + 1):
            lkup_key = base_lkup_key + '&' + str(time)
            bs_key = base_bs_key + '&' + str(time)
            BossLookup.objects.create(lookup_key=lkup_key, boss_key=bs_key,
                                      collection_name=col.name,
                                      experiment_name=exp.name,
                                      channel_layer_name=layer.name
                                      )

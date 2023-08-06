-- update cards set config = json_build_object() where config is null;
-- update cards as c
-- set config = jsonb_set(config, '{uniqueTiles}', to_jsonb(json_build_array()), true);
-- update cards as c
-- set config = jsonb_set(config, '{uniqueToAllInstances}', to_jsonb(false), true);
-- select * from cards where config is not null;

-- delete from tile_revision_log where survey_id = '94c16e28-f6e2-47a3-8177-5460631bc479';
-- delete from mobile_sync_log where survey_id = '94c16e28-f6e2-47a3-8177-5460631bc479';
-- delete from resource_revision_log where survey_id = '94c16e28-f6e2-47a3-8177-5460631bc479';

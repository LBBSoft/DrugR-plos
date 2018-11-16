create procedure drug_repurpose_transporters @drug char(500), @c int, @knw_action varchar(20)
as
begin
    if @c=1 begin
		select fr.*,t2.num_of_trgt from (select distinct fres.* from (select res.*,dta.transporter_action from 
		(select d.id as 'drug_id',d.drug_name,transporter_id,transporter_name,t.organism from drugs as d 
		inner join drug_transporters as t on t.drug_id=d.id 
		where known_action like '%'+@knw_action+'%' and transporter_id in (select transporter_id from drug_transporter_actions 
		where drug_id in(select id from drugs where drug_name =@drug))) as res 
		inner join drug_transporter_actions as dta on res.drug_id=dta.drug_id and res.transporter_id=dta.transporter_id) as fres,drug_transporter_actions as dt
		where dt.drug_id in (select id from drugs where drug_name =@drug) 
		and dt.transporter_id = fres.transporter_id and dt.transporter_action=fres.transporter_action) as fr 
		inner join (select drug_id,count(*) as num_of_trgt from drug_transporters group by drug_id) as t2 on t2.drug_id=fr.drug_id
		where fr.drug_id not in (select id from drugs where drug_name =@drug) 
	end
	else if @c=2 begin
		select fr.*,t2.num_of_trgt from (select distinct fres.* from (select res.*,dta.transporter_action from 
		(select d.id as 'drug_id',d.drug_name,transporter_id,transporter_name,t.organism from drugs as d 
		inner join drug_transporters as t on t.drug_id=d.id 
		where known_action like '%'+@knw_action+'%' and transporter_id in (select transporter_id from drug_transporter_actions 
		where drug_id in(select id from drugs where drug_name =@drug))) as res 
		inner join drug_transporter_actions as dta on res.drug_id=dta.drug_id and res.transporter_id=dta.transporter_id) as fres,drug_transporter_actions as dt
		where dt.drug_id in (select id from drugs where drug_name =@drug) 
		and dt.transporter_id = fres.transporter_id and dt.transporter_action=fres.transporter_action) as fr 
		inner join (select drug_id,count(*) as num_of_trgt from drug_transporters group by drug_id) as t2 on t2.drug_id=fr.drug_id
		where fr.drug_id not in (select id from drugs where drug_name =@drug) 
		and fr.drug_id in (select id from drug_properties where FDA_label<>'unknown')
	end
	else if @c=3 begin
		select fr.*,t2.num_of_trgt from (select distinct fres.* from (select res.*,dta.transporter_action from 
		(select d.id as 'drug_id',d.drug_name,transporter_id,transporter_name,t.organism from drugs as d 
		inner join drug_transporters as t on t.drug_id=d.id 
		where known_action like '%'+@knw_action+'%' and transporter_id in (select transporter_id from drug_transporter_actions 
		where drug_id in(select id from drugs where drug_name =@drug))) as res 
		inner join drug_transporter_actions as dta on res.drug_id=dta.drug_id and res.transporter_id=dta.transporter_id) as fres,drug_transporter_actions as dt
		where dt.drug_id in (select id from drugs where drug_name =@drug) 
		and dt.transporter_id = fres.transporter_id and dt.transporter_action=fres.transporter_action) as fr 
		inner join (select drug_id,count(*) as num_of_trgt from drug_transporters group by drug_id) as t2 on t2.drug_id=fr.drug_id
		where fr.drug_id not in (select id from drugs where drug_name =@drug) 
		and fr.drug_id in (select id from drug_properties where FDA_label='unknown')
	end
end

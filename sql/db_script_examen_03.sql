
CREATE TABLE horario (
  "id_horario" serial PRIMARY KEY,
  "hora_pico" varchar not null,
  "hora_inicio" time not null,
  "hora_fin" time not null
  
);
ALTER TABLE horario ADD CONSTRAINT uk_id_horario UNIQUE ("id_horario");

comment on table horario is 'registro sobre de horarios';
comment on column horario.id_horario is 'primary key de la tabla horario'; 
comment on column horario.hora_pico is 'es hora pico [si/no]';
comment on column horario.hora_inicio is 'hora de inicio)';
comment on column horario.hora_fin is 'hora de finalizacion';


CREATE TABLE cargador (
  "id_cargador" serial PRIMARY KEY,
  "estado" varchar not null
);
alter table cargador add constraint uk_id_cargador unique ("id_cargador");

comment on table cargador is 'registro sobre el cargador';
comment on column cargador.id_cargador is 'primary key de la tabla cargador';
comment on column cargador.estado is 'estado del cargador [ocupado/desocupado]';

CREATE table autobus (
  "id_autobus" serial PRIMARY KEY,
  "estado" varchar not null
);
alter table autobus add constraint uk_id_autobus unique ("id_autobus");

comment on table autobus is 'registro de autobuses ';
comment on column autobus.id_autobus is 'primary key de la tabla autobus';
comment on column autobus.estado is 'estado del autobus [parqueado/cargando/operando]';


CREATE TABLE uso_cargador_bus (
  "id_uso_cargador_bus" serial PRIMARY KEY,
  "horario_fk" int not null,
  "cargador_fk" int not null,
  "autobus_fk" int not null
);
alter table uso_cargador_bus add constraint uk_id_uso_cargador_bus unique ("id_uso_cargador_bus");

comment on table uso_cargador_bus is 'registro del funcionamiento de los cargadores';
comment on column uso_cargador_bus.id_uso_cargador_bus is 'primary key de la tabla uso_cargador_bus';
comment on column uso_cargador_bus.horario_fk is 'clave foranea asociada a la tabla horario';
comment on column uso_cargador_bus.cargador_fk is 'clave foranea asociada a la tabla cargador';
comment on column uso_cargador_bus.autobus_fk is 'clave foranea asociada a la tabla autobus';


ALTER TABLE uso_cargador_bus ADD FOREIGN KEY ("horario_fk") REFERENCES horario ("id_horario");

ALTER TABLE uso_cargador_bus ADD FOREIGN KEY ("cargador_fk") REFERENCES cargador ("id_cargador");

ALTER TABLE uso_cargador_bus ADD FOREIGN KEY ("autobus_fk") REFERENCES autobus ("id_autobus");

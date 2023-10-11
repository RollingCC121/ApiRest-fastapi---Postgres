CREATE TABLE programacion_autobuses (
  "id_programacion_autobuses" serial PRIMARY KEY,
  "autobus_fk" int not null,
  "horario_fk" int not null
);
ALTER TABLE programacion_autobuses ADD CONSTRAINT uk_id_programacion_autobuses UNIQUE ("id_programacion_autobuses");
ALTER TABLE programacion_autobuses ADD CONSTRAINT uk_autobus_fk UNIQUE ("autobus_fk");
ALTER TABLE programacion_autobuses ADD CONSTRAINT uk_horraio_fk UNIQUE ("horario_fk");

comment on table programacion_autobuses is 'registro sobre la programacion de los autobuses';
comment on column programacion_autobuses.id_programacion_autobuses is 'primary key de la tabla programacion_autobuses'; 
comment on column programacion_autobuses.autobus_fk is 'fk asociada a la tabla autobus(id_autobus)';
comment on column programacion_autobuses.horario_fk is 'fk asociada a la tabla horario(id_horario)';


CREATE TABLE cargador (
  "id_cargador" serial PRIMARY KEY,
  "autobus_fk" int not null
);
alter table cargador add constraint uk_id_cargador unique ("id_cargador");
--alter table cargador add constraint uk_autobus_fk unique ("autobus_fk");

comment on table cargador is 'registro sobre el funcionamiento del cargador';
comment on column cargador.id_cargador is 'primary key de la tabla cargador';
comment on column cargador.autobus_fk is 'fk asociada a la tabla autobus(id_autobus)';

CREATE TABLE horario (
  "id_horario" serial PRIMARY KEY,
  "hora" time not null,
  "hora_pico" varchar not null
);
alter table horario add constraint uk_id_horario unique ("id_horario");
alter table horario add constraint uk_hora unique ("hora");
alter table horario add constraint uk_hora_pico unique ("hora_pico");

comment on table horario is 'registro del horario de funcionamiento de los servicios';
comment on column horario.id_horario is 'primary key de la tabla horario';
comment on column horario.hora is 'hora de funcionamiento';
comment on column horario.hora_pico is 'es hora pico [si/no]';

CREATE TABLE autobus (
  "id_autobus" serial PRIMARY KEY,
  "placa" varchar not null,
  "marca" varchar not null,
  "ruta" varchar not null
);
alter table autobus add constraint uk_id_autobus unique ("id_autobus");
alter table autobus add constraint uk_placa unique ("placa");
alter table autobus add constraint uk_marca unique ("marca");
alter table autobus add constraint uk_ruta unique ("ruta");

comment on table autobus is 'registro de autobuses';
comment on column autobus.id_autobus is 'primary key de la tabla autobus';
comment on column autobus.placa is 'placa del autobus';
comment on column autobus.marca is 'marca del autobus';
comment on column autobus.ruta is 'ruta del autobus';

CREATE TABLE programacion_cargadores (
  "id_programacion_cargadores" serial PRIMARY KEY,
  "horario_fk" int not null,
  "autobus_fk" int not null
);
alter table programacion_cargadores add constraint uk_id_programacion_cargadores unique ("id_programacion_cargadores");
alter table programacion_cargadores add constraint uk_horario_fk unique ("horario_fk");
--alter table programacion_cargadores add constraint uk_autobus_fk unique ("autobus_fk");

comment on table programacion_cargadores is 'registro de la programacion de los cargadores';
comment on column programacion_cargadores.id_programacion_cargadores is 'primary key de la tabla programacion_cargadores';
comment on column programacion_cargadores.horario_fk is 'fk asociada a la tabla horario(id_horario)';
comment on column programacion_cargadores.autobus_fk is 'fk asociada a la tabla autobus(id_autobus)';


ALTER TABLE programacion_cargadores ADD FOREIGN KEY ("horario_fk") REFERENCES horario ("id_horario");

ALTER TABLE programacion_cargadores ADD FOREIGN KEY ("autobus_fk") REFERENCES autobus ("id_autobus");

ALTER TABLE cargador ADD FOREIGN KEY ("autobus_fk") REFERENCES autobus ("id_autobus");

ALTER TABLE programacion_autobuses ADD FOREIGN KEY ("autobus_fk") REFERENCES autobus ("id_autobus");

ALTER TABLE programacion_autobuses ADD FOREIGN KEY ("horario_fk") REFERENCES horario ("id_horario");
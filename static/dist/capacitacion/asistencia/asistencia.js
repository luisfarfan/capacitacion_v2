/**
 * Created by lfarfan on 05/12/2016.
 */
$(function () {
    getLocales();
});

var turno;
$('#local').change(e=> {
    "use strict";
    let id_local = $('#local').val();
    getAmbientes(id_local);
    getRangoFechas(id_local);
});

function disabledTurnos(turno) {
    if (turno == '0') {
        $('input[name="turno_mañana"]').map((key, val)=> {
            "use strict";
            $(val).prop('disabled', false);
        });
        $('input[name="turno_tarde"]').map((key, val)=> {
            "use strict";
            $(val).prop('disabled', true);
        });
    } else if (turno == '1') {
        $('input[name="turno_mañana"]').map((key, val)=> {
            "use strict";
            $(val).prop('disabled', true);
        });
        $('input[name="turno_tarde"]').map((key, val)=> {
            "use strict";
            $(val).prop('disabled', false);
        });
    }
}

function getRangoFechas(id_local) {
    "use strict";
    $.ajax({
        url: `${BASEURL}/getRangeDatesLocal/${id_local}/`,
        type: 'GET',
        success: response => {
            setSelect_v2('fechas', response.fechas);
            turno = response.turno;
        },
        error: error => {
            console.log(error);
        }
    });
}

function getLocales() {
    "use strict";
    let ubigeo = `${session.ccdd}${session.ccpp}${session.ccdi}`;
    $.ajax({
        url: `${BASEURL}/localbyzona/${ubigeo}/${session.zona}/`,
        type: 'GET',
        success: response => {
            setSelect_v2('local', response, ['id_local', 'nombre_local'])
        },
        error: error => {
            console.log('ERROR!!', error)
        }
    })
}
function getAmbientes(id_local) {
    "use strict";
    $.ajax({
        url: `${BASEURL}/localambiente/${id_local}/`,
        type: 'GET',
        success: response => {
            console.log(response);
            setTable('tabla_detalle_ambientes', response, ['numero', 'capacidad', 'nombre_ambiente', {pk: 'id_localambiente'}]);
        },
        error: error => {
            console.log('ERROR!!', error);
        }
    })
}

function getPEA(id_ambiente) {
    "use strict";
    let params = ['nombre', 'cargo'];
    $.ajax({
        url: `${BASEURL}/rest/pea_aula/${id_ambiente}/`,
        type: 'GET',
        success: response => {
            let json = {};
            console.log(response);
            let html = '';
            $.each(response.pea, (key, val)=> {
                html += '<tr>';
                html += `<td>${key + 1}</td>`;
                for (let i in params) {
                    html += `<td>${val[params[i]]}</td>`;
                }
                html += `<td><div class="form-group">
										<div class="checkbox checkbox-right">
											<label>
												<input type="radio" name="turno_mañana" value="0">
												Normal
											</label>
										</div>

										<div class="checkbox checkbox-right">
											<label>
												<input type="radio" name="turno_mañana" value="1">
												Tardanza
											</label>
										</div>
										<div class="checkbox checkbox-right">
											<label>
												<input type="radio" name="turno_mañana" value="2">
                                                Falta
											</label>
										</div>
									</div></td>`;
                html += `<td><div class="form-group">
										<div class="checkbox checkbox-right">
											<label>
												<input type="radio" name="turno_tarde" value="0">
												Normal
											</label>
										</div>

										<div class="checkbox checkbox-right">
											<label>
												<input type="radio" name="turno_tarde" value="1">
												Tardanza
											</label>
										</div>
										<div class="checkbox checkbox-right">
											<label>
												<input type="radio" name="turno_tarde" value="2">
                                                Falta
											</label>
										</div>
									</div></td>`;
                html += '</tr>';

            });
            json.html = html;
            setTable('tabla_pea', json);
            disabledTurnos(turno);

        },
        error: error => {
            console.log('ERROR!!', error)
        }
    })
}
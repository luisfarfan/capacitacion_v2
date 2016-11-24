/**
 * Created by LFarfan on 24/11/2016.
 */
$('#etapa').trigger('change');
$('#etapa').change(function () {
    "use strict";
    getCursos($(this).val());
});
$('#btn_registrar_criterio').on('click', ()=>$('#modal_registrar_criterio').modal('show'));

function getCursos(idetapa) {
    "use strict";
    let html = '';
    $.getJSON(`${BASE_URL}cursobyetapa/${idetapa}`, data=> {
        let descripcion_curso = '';
        let cursoslice = '';
        $.each(data, (key, val)=> {
            cursoslice = val.nombre_curso.slice(9)
            descripcion_curso = idetapa == 1 ? `Curso Dirigido a ${cursoslice} para el Censo Experimental` : `Curso Dirigido a ${cursoslice} para el Empadronamiento`;
            html += `<tr><td>${val.nombre_curso}</td><td>${descripcion_curso}</td><td>
                <button type="button" class="btn btn-danger btn-rounded legitRipple">Registrar Evaluaciones</button>
                </td></tr>`
        });
        $('#tabla_curso').find('tbody').html(html);
    });
}

function getCriterios() {
    "use strict";
    let html = '';
    $.getJSON(`${BASE_URL}rest/criterios/${idetapa}`, data=> {
        $.each(data, (key, val)=> {
            html += `<tr><td>${key}</td><td>${val.descripcion_criterio}</td>
                <td>
                <button type="button" class="btn btn-danger btn-rounded legitRipple">Editar</button>
                <button type="button" class="btn btn-danger btn-rounded legitRipple">Eliminar</button>
                </td></tr>`
        });
        $('#tabla_criterios').find('tbody').html(html);
    });
}
/**
 * Created by LFarfan on 24/11/2016.
 */
$(function () {
    "use strict";
    getCriterios();
});
$('#etapa').trigger('change');
$('#etapa').change(function () {
    "use strict";
    getCursos($(this).val());
});
$('#btn_registrar_criterio').on('click', ()=> {
    "use strict";
    getCriterios();
    $('#modal_registrar_criterio').modal('show')
});
function setSelect(id, json, select2 = false) {
    $('#' + id).find('option').remove();
    let html = '';
    $.each(json, function (key, val) {
        html += `<option value="${val.id}">${val.text}</option>`
    });
    $('#' + id).html(html);
    select2 ? $('#' + id).select2() : '';
}
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
                <button onclick="registrarEvaluacion(${val.id_curso},${val.nota_minima})" type="button" class="btn btn-danger btn-rounded legitRipple">Registrar Evaluaciones</button>
                </td></tr>`
        });
        $('#tabla_curso').find('tbody').html(html);
    });
}

function getCriterios() {
    "use strict";
    let html = '';
    $.getJSON(`${BASE_URL}rest/criterio/`, data=> {
        let json = [{id: '', text: 'Seleccione'}];
        $.each(data, (key, val)=> {
            html += `<tr><td>${key}</td><td>${val.nombre_criterio}</td>
                <td>${val.descripcion_criterio}</td>
                <td>
                    <ul class="icons-list">
                        <li><a onclick="editarCriterio(this,${val.id_criterio})" href="#"><i class="icon-pencil7"></i></a></li>
                        <li><a onclick="eliminarCriterio(${val.id_criterio})" href="#"><i class="icon-trash"></i></a></li>
					</ul>
                </td></tr>`
            json.push({id: val.id_criterio, text: val.nombre_criterio});
        });
        setSelect('id_criterio2', json);
        $('#tabla_criterios').find('tbody').html(html);
    });
}


$('#btn_registrarcriterio').on('click', function () {
    $('#modalform_registrar_criterio').modal('show');
    setFormCriterio('', '', '');

});

function setFormCriterio(id, nombre, criterio) {
    $('#nombre_criterio').val(nombre)
    $('#descripcion_criterio').val(criterio)
    $('#id_criterio').val(id)
}

var validator = $("#form_registrarcriterio").validate({
    ignore: 'input[type=hidden], .select2-search__field', // ignore hidden fields
    errorClass: 'validation-error-label',
    successClass: 'validation-valid-label',
    highlight: function (element, errorClass) {
        $(element).removeClass(errorClass);
    },
    unhighlight: function (element, errorClass) {
        $(element).removeClass(errorClass);
    },

    // Different components require proper error label placement
    errorPlacement: function (error, element) {

        // Styled checkboxes, radios, bootstrap switch
        if (element.parents('div').hasClass("checker") || element.parents('div').hasClass("choice") || element.parent().hasClass('bootstrap-switch-container')) {
            if (element.parents('label').hasClass('checkbox-inline') || element.parents('label').hasClass('radio-inline')) {
                error.appendTo(element.parent().parent().parent().parent());
            } else {
                error.appendTo(element.parent().parent().parent().parent().parent());
            }
        }

        // Unstyled checkboxes, radios
        else if (element.parents('div').hasClass('checkbox') || element.parents('div').hasClass('radio')) {
            error.appendTo(element.parent().parent().parent());
        }

        // Input with icons and Select2
        else if (element.parents('div').hasClass('has-feedback') || element.hasClass('select2-hidden-accessible')) {
            error.appendTo(element.parent());
        }

        // Inline checkboxes, radios
        else if (element.parents('label').hasClass('checkbox-inline') || element.parents('label').hasClass('radio-inline')) {
            error.appendTo(element.parent().parent());
        }

        // Input group, styled file input
        else if (element.parent().hasClass('uploader') || element.parents().hasClass('input-group')) {
            error.appendTo(element.parent().parent());
        } else {
            error.insertAfter(element);
        }
    },
    validClass: "validation-valid-label",
    success: function (label) {
        label.addClass("validation-valid-label").text("Success.")
    },
    messages: {
        custom: {
            required: "El campo es requerido",
        },
        agree: "Please accept our policy"
    }
});

$('#submit_registrarcriterio').on('click', ()=> {
    "use strict";
    validator.form();
    if (validator.numberOfInvalids() == 0) {
        saveCriterio();
    }
});

function saveCriterio() {
    "use strict";
    let data = {};
    $('#form_registrarcriterio').serializeArray().map(res=> {
        data[res.name] = res.value;
    });
    var options = {
        url: '',
        method: '',
        data: {},
        success: function () {
            getCriterios();
            $('#modalform_registrar_criterio').modal('hide');
        },
    };
    if ($('#id_criterio').val() != '') {
        options.method = 'PUT';
        options.url = `${BASE_URL}rest/criterio/${$('#id_criterio').val()}/`;
        options.data = data;
    } else {
        options.method = 'POST';
        options.url = `${BASE_URL}rest/criterio/`;
        options.data = data;
    }
    $.ajax(options);
}

function editarCriterio(elemento, id_criterio) {
    "use strict";

    let tr = $(elemento).parent().parent().parent().parent();
    setFormCriterio(id_criterio, tr.find('td').eq(1).text(), tr.find('td').eq(2).text());

    $('#modalform_registrar_criterio').modal('show');
}

function eliminarCriterio(id_criterio) {
    "use strict";
    bootbox.confirm("¿Esta usted seguro de Eliminar este Criterio?", result=> {
        if (result) {
            $.ajax({
                url: `${BASE_URL}rest/criterio/${id_criterio}/`,
                type: 'DELETE',
                success: response=> {
                    console.log(response);
                    getCriterios();
                }
            })
        }
    })
}

function registrarEvaluacion(id_curso, nota_minima) {
    "use strict";
    $('#modal_evaluacioncurso').modal('show');
    $('#nota_minima').val(nota_minima);
    $('#id_curso').val(id_curso);
}
$('#btn_guardarnotaminima').on('click', ()=> {
    "use strict";
    saveNotaMinima();
});

function saveNotaMinima() {
    "use strict";
    bootbox.confirm("¿Esta usted seguro de cambiar la Nota Mínima?", result=> {
        if (result) {
            let id_curso = $('#id_curso').val();
            $.ajax({
                url: `${BASE_URL}rest/cursos/${id_curso}/`,
                type: 'PATCH',
                data: {nota_minima: $('#nota_minima').val()},
                success: response => {
                    console.log(response);
                },
            })
        }
    });
}

$('#registrar_aulas_modal').on('click', function () {
    let ambientescheck = $('#ambientesdata :input[type="checkbox"]');
    $('#id_ambiente').find('option').remove();
    let data = [];
    $.each(ambientescheck, function (key, val) {
        let texto = $(val).parent().parent().parent().text();
        let id = parseInt(key) + 1;
        $(val).is(':checked') ? data.push({id: id, text: texto.trim()}) : '';
    });
    $('#id_ambiente').select2({data: data});
    getLocalAmbientes();
});

function setLocalAmbienteForm(id_localambiente) {
    $('#id_localambiente').val(id_localambiente);
    $.uniform.update()
    let url = `${BASE_URL}rest/localambiente/${id_localambiente}/`;
    $.getJSON(url, data=> {
        "use strict";
        console.log(data);
        $.each(data, (key, val)=> {
            console.log($(`input[name=${key}]`),key,val);
            if ($(`input[name=${key}]`).is(":checkbox") && $(`input[name=${key}]`).val() == "1") {
                console.log($(`input[name=${key}]`).is(":checkbox"));
                console.log($(`input[name=${key}]`).val() == "1");
                $(`input[name=${key}]`).prop('checked', true);
                $.uniform.update()
            } else {
                $(`input[name=${key}]`).val(val);
            }
        });

    });
}
function getLocalAmbientes() {
    let id_local = $('#id_local').val();
    let url = `${BASE_URL}localambiente/${id_local}/`;
    $('#tabla_aulas').find('tbody').empty();
    $.getJSON(url, function (data) {
        if (data.length > 0) {
            let html = '';
            $.each(data, function (key, val) {
                let ambiente = '';
                switch (val.id_ambiente) {
                    case "1":
                        ambiente = 'Aula';
                        break;
                    case "2":
                        ambiente = 'Auditorios';
                        break;
                    case "3":
                        ambiente = 'Sala Reunion';
                        break;
                    case "4":
                        ambiente = 'Oficina Administrativa';
                        break;
                    case "5":
                        ambiente = 'Otros';
                        break;
                }
                html = `<tr><td>${val.numero}</td><td>${ambiente}</td><td>${val.capacidad}</td><td><button onclick="setLocalAmbienteForm(${val.id_localambiente})">Editar</button></td></tr>`;
            });
            $('#tabla_aulas').find('tbody').html(html);
            $('#tabla_aulas').DataTable();
        }
    });
}

var validator_aula = $(".form-validate-aula").validate({
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
    rules: {
        mesas_cant: {
            range: [0, 50]
        },
        sillas_cant: {
            range: [0, 50]
        },
        carpindividuales_cant: {
            range: [0, 50]
        },
        carpbipersonales_cant: {
            range: [0, 50]
        },
        numero: {
            range: [0, 99]
        },
        n_piso: {
            range: [0, 10]
        },
        capacidad: {
            range: [0, 500]
        },
    },
    messages: {
        custom: {
            required: "El campo es requerido",
        },
        agree: "Please accept our policy"
    }
});

$('#registrar_aula_submit').on('click', ()=> {
    "use strict";
    validator_aula.form();
    validator_aula.showErrors();
    let url = '';
    let method = '';
    let title = '';
    let text = '';
    let title_entry = '';
    if ($('#id_localambiente').val() != '') {
        url = `${BASE_URL}rest/localambiente/${$('#id_localambiente').val()}/`;
        method = 'PUT';
        title = 'Edición!';
        text = 'El Aula se ha editado con exito!';
        title_entry = 'Esta usted seguro de Editar el Aula?'
    } else {
        url = `${BASE_URL}rest/localambiente/`;
        method = 'POST';
        title = 'Agregado!';
        text = 'El Aula se ha Agregado con exito!';
        title_entry = 'Esta usted seguro de Agregar el Aula?'
    }
    if (validator_aula.numberOfInvalids() == 0) {
        swal({
            title: title_entry,
            text: "",
            type: "success",
            showCancelButton: true,
            confirmButtonColor: "#EF5350",
            confirmButtonText: "Si!",
            cancelButtonText: "No, Cancelar!",
            closeOnConfirm: false,
            closeOnCancel: false
        }, function (isConfirm) {
            if (isConfirm) {
                let id_localambiente = $('#id_localambiente').val();
                let form_data = $('#form_aula').serializeArray();
                let dataupdate = {};
                dataupdate['id_local'] = $('#id_local').val();
                $.each(form_data, function (key, val) {
                    val.value == "on" ? dataupdate[val.name] = 1 : dataupdate[val.name] = val.value;
                });
                $.ajax({
                    url: url,
                    type: method,
                    data: dataupdate,
                    success: function (data) {
                        swal({
                            title: title,
                            text: text,
                            confirmButtonColor: "#66BB6A",
                            type: "success"
                        });
                        console.log(data);
                        getLocalAmbientes();
                        validator_aula.resetForm();
                        $.uniform.update();
                    }
                })
            } else {
                swal({
                    title: "Cancelado",
                    text: "La acción fue cancelada",
                    confirmButtonColor: "#2196F3",
                    type: "error"
                });
            }
        });
    }

});



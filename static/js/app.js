let tipoOperacion = "";

document.addEventListener("DOMContentLoaded", function () {
  cargarCuentas();

  document.getElementById("btnBalance").addEventListener("click", function () {
    mostrarModalBalance();
  });

  document.getElementById("btnDeposito").addEventListener("click", function () {
    abrirModalOperacion("deposit");
  });

  document.getElementById("btnRetiro").addEventListener("click", function () {
    abrirModalOperacion("withdraw");
  });
});

function cerrarModal(id) {
  $("#" + id).modal("hide");
}

function abrirModalOperacion(tipo) {
  tipoOperacion = tipo;
  document.getElementById("modalOperacionTitle").textContent =
    tipo === "retiro" ? "Retirar Dinero" : "Realizar Depósito";
  $("#modalOperacion").modal("show");
}

function cargarCuentas() {
  fetch("http://localhost:8000/accounts/")
    .then((response) => response.json())
    .then((data) => {
      const selectBalance = document.getElementById("accountsBalance");
      const selectOperacion = document.getElementById("accountsOperacion");

      data.forEach((cuenta) => {
        // Opción para el select de balance
        const optionBalance = document.createElement("option");
        optionBalance.value = cuenta.id;
        optionBalance.textContent =
          cuenta.account_number + " - " + cuenta.owner_name;
        selectBalance.appendChild(optionBalance);

        // Opción para el select de operación
        const optionOperacion = document.createElement("option");
        optionOperacion.value = cuenta.id;
        optionOperacion.textContent =
          cuenta.account_number + " - " + cuenta.owner_name;
        selectOperacion.appendChild(optionOperacion);
      });
    })
    .catch((error) => {
      console.error("Error al cargar las cuentas:", error);
    });
}

function mostrarModalBalance() {
  $("#modalBalance").modal("show");
}

function cerrarModalBalance() {
  $("#modalBalance").modal("hide");
}

function consultarBalance() {
  const accountId = document.getElementById("accountsBalance").value;
  axios
    .get("http://localhost:8000/accounts/" + accountId + "/balance", {
      account_id: accountId,
    })
    .then((response) => {
      cerrarModalBalance();
      Swal.fire({
        title: "Balance Consultado",
        text: "Balance: " + response.data.balance + "$",
        icon: "success",
        confirmButtonText: "Ok",
      });
    })
    .catch((error) => {
      console.error("Error al realizar la solicitud:", error);
    });
}

function realizarOperacion() {
  const accountId = document.getElementById("accountsOperacion").value;
  const amount = document.getElementById("amountOperacion").value;

  axios
    .post("http://localhost:8000/transactions/", {
      account_id: parseInt(accountId),
      amount: parseFloat(amount),
      transaction_type: tipoOperacion,
    })
    .then((response) => {
      // Aquí manejas la respuesta exitosa
      Swal.fire({
        title: "Operación Exitosa",
        text: "Transacción realizada con éxito",
        icon: "success",
        confirmButtonText: "Ok",
      });
    })
    .catch((error) => {
      // Aquí manejas los errores
      Swal.fire({
        title: "Error en la Operación",
        text: error.response.data.detail || "Ha ocurrido un error",
        icon: "error",
        confirmButtonText: "Cerrar",
      });
    });

  cerrarModal("modalOperacion");
}
// Funciones para depositar y retirar

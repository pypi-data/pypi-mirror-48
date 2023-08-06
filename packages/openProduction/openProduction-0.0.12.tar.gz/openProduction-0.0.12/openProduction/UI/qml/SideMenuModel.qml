import QtQuick 2.0

ListModel {
    ListElement {
        name: "Dashboard"
        iconName: "icons/dashboard.png"
        menuTitle: "Dashboard"
        section: "Produktion"
        source: "Dashboard/Dashboard.qml"
        role: "PRODUCTION,MANAGER"
    }
    ListElement {
        name: "Rüsten"
        iconName: "icons/import.png"
        menuTitle: "Produkt rüsten"
        section: "Produktion"
        source: "ProductRun/ProductEquip.qml"
        role: "PRODUCTION"
    }
    ListElement {
        name: "Ändern"
        iconName: "icons/change.png"
        menuTitle: "Produkt ändern"
        section: "Produkt"
        source: "Dashboard/Dashboard.qml"
        role: "PRODUCTION"
    }
    ListElement {
        name: "Erstellen"
        iconName: "icons/create.png"
        menuTitle: "Produkt erstellen"
        section: "Produkt"
        source: "Dashboard/Dashboard.qml"
        role: "PRODUCTION"
    }
    ListElement {
        name: "Exportieren"
        iconName: "icons/export.png"
        menuTitle: "Daten exportieren"
        section: "Reports"
        source: "Dashboard/Dashboard.qml"
        role: "PRODUCTION,MANAGER"
    }
    ListElement {
        name: "Installation"
        iconName: "icons/install.png"
        menuTitle: "Installation"
        section: "Sonstiges"
        source: "Installation.qml"
        role: "PRODUCTION,MANAGER"
    }
}

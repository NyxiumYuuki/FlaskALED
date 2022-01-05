import {AfterViewInit, Component, ViewChild} from '@angular/core';
import {MatTableDataSource} from "@angular/material/table";
import {FictitiousDatasService} from "../../../common/services/fictitiousDatas/fictitious-datas.service";
import {MatSort} from "@angular/material/sort";
import {MatPaginator} from "@angular/material/paginator";
import {MatDialog} from "@angular/material/dialog";
import {PopupCreatePersonComponent} from "../popup-create-person/popup-create-person.component";
import {MatSnackBar} from "@angular/material/snack-bar";
import {PopupUpdatePersonAdminComponent} from "../popup-update-person-admin/popup-update-person-admin.component";
import {PopupDeleteProfilComponent} from "../../../common/components/popup-delete-profil/popup-delete-profil.component";



@Component({
  selector: 'app-page-user-list',
  templateUrl: './page-user-list.component.html',
  styleUrls: ['./page-user-list.component.scss']
})
export class PageUserListComponent implements AfterViewInit
{
    displayedColumns: string[] = [ "nickname", "email", "role", "actions" ];
    dataSource: MatTableDataSource<any> = new MatTableDataSource<any>();
    @ViewChild(MatSort) sort: MatSort;
    @ViewChild(MatPaginator) paginator: MatPaginator;
    configSnackBar = { duration: 2000, panelClass: "custom-class" };


    constructor( private fictitiousDatasService: FictitiousDatasService,
                 public dialog: MatDialog,
                 private snackBar: MatSnackBar) { }


    ngAfterViewInit(): void
    {
        // Faux code
        let tabPerson = this.fictitiousDatasService.getTabPerson(5);

        // Vrai code ...
        tabPerson = tabPerson.map( person => {
            if(!person.is_admin) return Object.assign(person, {role: "utilisateur"});
            else return Object.assign(person, {role: "admin"});
        });
        this.dataSource = new MatTableDataSource(tabPerson);
        this.dataSource.sort = this.sort;
        this.dataSource.paginator = this.paginator;
    }


    applyFilter(event: Event)
    {
        const filterValue = (event.target as HTMLInputElement).value;
        this.dataSource.filter = filterValue.trim().toLowerCase();
    }


    // Appuie sur le bouton "add"
    onAdd(): void
    {
        const config = { width: '50%' };
        this.dialog
            .open(PopupCreatePersonComponent, config)
            .afterClosed()
            .subscribe( person => {

                if((person === null) || (person === undefined)) {
                    this.snackBar.open( "Opération annulée", "", this.configSnackBar);
                }
                else {
                    this.dataSource.data.push(person);
                    this.dataSource.data = this.dataSource.data;
                    this.dataSource = this.dataSource;
                    this.snackBar.open( "L'utilisateur a bien été créé ✔", "", this.configSnackBar);
                }
            });
    }


    // Appuie sur le bouton "edit"
    onUpdate(personToUpdate: any): void
    {
        const config = {
            width: '50%',
            data: { person: personToUpdate }
        };
        this.dialog
            .open(PopupUpdatePersonAdminComponent, config)
            .afterClosed()
            .subscribe( personUpdated => {

                if((personUpdated === null) || (personUpdated === undefined)) {
                    this.snackBar.open( "Opération annulée", "", this.configSnackBar);
                }
                else {
                    const index = this.dataSource.data.findIndex( elt => (elt.id === personToUpdate.id));
                    this.dataSource.data.splice(index, 1, personUpdated);
                    this.dataSource.data = this.dataSource.data;
                    this.dataSource = this.dataSource;
                    this.snackBar.open( "L'utilisateur a bien été modifié ✔", "", this.configSnackBar);
                }

            });
    }


    // Appuie sur le bouton "delete"
    onDelete(personToDelete: any): void
    {
        const config = {
            data: {
                id: personToDelete.id,
                email: personToDelete.email,
                me: false,
            }
        };
        this.dialog
            .open(PopupDeleteProfilComponent, config)
            .afterClosed()
            .subscribe( personUpdated => {

                if((personUpdated === null) || (personUpdated === undefined)) {
                    this.snackBar.open( "Opération annulée", "", this.configSnackBar);
                }
                else {
                    const index = this.dataSource.data.findIndex( elt => (elt.id === personToDelete.id));
                    this.dataSource.data.splice(index, 1);
                    this.dataSource.data = this.dataSource.data;
                    this.dataSource = this.dataSource;
                    this.snackBar.open( "L'utilisateur a bien été supprimé ✔", "", this.configSnackBar);
                }

            });
    }

}

import { Component, OnInit } from '@angular/core';
import {Person} from "../../../interfaces/Person";
import {MatDialog} from "@angular/material/dialog";
import {MatSnackBar} from "@angular/material/snack-bar";
import {PopupUpdateProfilComponent} from "../popup-update-profil/popup-update-profil.component";
import {FictitiousDatasService} from "../../../services/fictitiousDatas/fictitious-datas.service";
import {Router} from "@angular/router";



@Component({
  selector: 'app-page-profil',
  templateUrl: './page-profil.component.html',
  styleUrls: ['./page-profil.component.scss']
})
export class PageProfilComponent implements OnInit
{
    person: Person = {
        id: "",
        login: "",
        email: "",
        hashPass: "",
        role: "user",
    };
    from: string = "" ;


    constructor( public dialog: MatDialog,
                 private snackBar: MatSnackBar,
                 private fictitiousDatasService: FictitiousDatasService,
                 private router: Router ) { }


    ngOnInit(): void
    {
        // faux code
        if(this.router.url.startsWith("/user")) {
            this.person = this.fictitiousDatasService.getUser();
            this.from = "user" ;
        }
        else if(this.router.url.startsWith("/admin")){
            this.person = this.fictitiousDatasService.getAdmin();
            this.from = "admin" ;
        }

        // Vrai code ...
    }


    // Appuie sur le bouton modifier
    onModifier(): void
    {
        const config = {
            width: '25%',
            data: { person: this.person }
        };
        this.dialog
            .open(PopupUpdateProfilComponent, config)
            .afterClosed()
            .subscribe(retour => this.onModifierCallback(retour));
    }


    // Callback de onModifier
    onModifierCallback(retour: any): void
    {
        if((retour === null) || (retour === undefined))
        {
            const config = { duration: 1000, panelClass: "custom-class" };
            this.snackBar.open( "Opération annulé", "", config);
        }
        else
        {
            this.person = retour;
        }
    }

}

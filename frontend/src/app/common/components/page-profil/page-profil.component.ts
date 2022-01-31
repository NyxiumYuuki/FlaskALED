import { Component, OnInit } from '@angular/core';
import {MatDialog} from "@angular/material/dialog";
import {MatSnackBar} from "@angular/material/snack-bar";
import {PopupUpdateProfilComponent} from "../popup-update-profil/popup-update-profil.component";
import {Router} from "@angular/router";
import {PopupDeleteProfilComponent} from "../popup-delete-profil/popup-delete-profil.component";
import {MessageService} from "../../services/message/message.service";
import {HttpParams} from "@angular/common/http";
import {ProfilService} from "../../services/profil/profil.service";



@Component({
  selector: 'app-page-profil',
  templateUrl: './page-profil.component.html',
  styleUrls: ['./page-profil.component.scss']
})
export class PageProfilComponent implements OnInit
{
    person = {
        id: "",
        nickname: "",
        email: "",
        is_admin: false,
    };
    from: string = "" ;
    configSnackbar = { duration: 3000, panelClass: "custom-class" };


    constructor( private messageService: MessageService,
                 private profilService: ProfilService,
                 public dialog: MatDialog,
                 private snackBar: MatSnackBar,
                 private router: Router ) { }


    ngOnInit(): void
    {
        if(this.router.url.startsWith("/user")) this.from = "user" ;
        else if(this.router.url.startsWith("/admin")) this.from = "admin" ;

        let params = new HttpParams()
        params = params.set("order_by", "nickname");
        params = params.set("id", this.profilService.getId());
        this.messageService
            .get("users", params)
            .subscribe(ret => this.ngOnInitCallback(ret), err => this.ngOnInitCallback(err));
    }


    // Callback de ngOnInit
    ngOnInitCallback(retour: any): void
    {
        if(retour.status !== "success") {
            console.log(retour);
        }
        else {
            this.person = retour.data[0];
        }
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
        if((retour === null) || (retour === undefined)) this.snackBar.open( "Opération annulé", "", this.configSnackbar);
        else if(retour.status === "success") this.person = retour.data;
    }


    // Appuie sur le bouton supprimer
    onSupprimer(): void
    {
        const config = {
            data: {
                id: this.person.id,
                email: this.person.email,
                me: true,
            }
        };
        this.dialog
            .open(PopupDeleteProfilComponent, config)
            .afterClosed()
            .subscribe(retour => this.onSupprimerCallback(retour));
    }


    // Callback de onSupprimer
    onSupprimerCallback(retour: any): void
    {
        if((retour === null) || (retour === undefined)) this.snackBar.open( "Opération annulé", "", this.configSnackbar);
        else if(retour.status === "error") this.snackBar.open(retour.error.message, "", this.configSnackbar);
        else if(retour.status === "success") this.router.navigateByUrl("/login");
    }

}

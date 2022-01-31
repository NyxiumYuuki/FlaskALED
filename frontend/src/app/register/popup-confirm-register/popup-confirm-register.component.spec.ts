import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PopupConfirmRegisterComponent } from './popup-confirm-register.component';

describe('PopupConfirmRegisterComponent', () => {
  let component: PopupConfirmRegisterComponent;
  let fixture: ComponentFixture<PopupConfirmRegisterComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PopupConfirmRegisterComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PopupConfirmRegisterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

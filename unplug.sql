PGDMP                         |            Unplug    14.2    14.2 +               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    26958    Unplug    DATABASE     l   CREATE DATABASE "Unplug" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';
    DROP DATABASE "Unplug";
                postgres    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
                postgres    false                       0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                   postgres    false    3            �            1259    27417    Menu    TABLE     �   CREATE TABLE public."Menu" (
    "Id" integer NOT NULL,
    "RestaurantId" integer NOT NULL,
    "CreatedAt" timestamp without time zone NOT NULL
);
    DROP TABLE public."Menu";
       public         heap    postgres    false    3            �            1259    27429 	   MenuGroup    TABLE     �   CREATE TABLE public."MenuGroup" (
    "Id" integer NOT NULL,
    "Name" character varying NOT NULL,
    "SortOrder" integer NOT NULL,
    "MenuId" integer NOT NULL
);
    DROP TABLE public."MenuGroup";
       public         heap    postgres    false    3            �            1259    27442    MenuGroupItemMap    TABLE     r   CREATE TABLE public."MenuGroupItemMap" (
    "MenuGroupId" integer NOT NULL,
    "MenuItemId" integer NOT NULL
);
 &   DROP TABLE public."MenuGroupItemMap";
       public         heap    postgres    false    3            �            1259    27428    MenuGroup_Id_seq    SEQUENCE     �   CREATE SEQUENCE public."MenuGroup_Id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public."MenuGroup_Id_seq";
       public          postgres    false    216    3                       0    0    MenuGroup_Id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public."MenuGroup_Id_seq" OWNED BY public."MenuGroup"."Id";
          public          postgres    false    215            �            1259    27401    MenuItem    TABLE     |  CREATE TABLE public."MenuItem" (
    "Id" integer NOT NULL,
    "Name" character varying NOT NULL,
    "Description" character varying,
    "StockStatus" character varying NOT NULL,
    "RestaurantId" integer NOT NULL,
    "Image" character varying,
    "Ranking" integer,
    "Price" double precision NOT NULL,
    "Calorie" double precision,
    "IsDeleted" boolean NOT NULL
);
    DROP TABLE public."MenuItem";
       public         heap    postgres    false    3            �            1259    27400    MenuItem_Id_seq    SEQUENCE     �   CREATE SEQUENCE public."MenuItem_Id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public."MenuItem_Id_seq";
       public          postgres    false    212    3                        0    0    MenuItem_Id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public."MenuItem_Id_seq" OWNED BY public."MenuItem"."Id";
          public          postgres    false    211            �            1259    27416    Menu_Id_seq    SEQUENCE     �   CREATE SEQUENCE public."Menu_Id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public."Menu_Id_seq";
       public          postgres    false    3    214            !           0    0    Menu_Id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public."Menu_Id_seq" OWNED BY public."Menu"."Id";
          public          postgres    false    213            �            1259    27392 
   Restaurant    TABLE     g   CREATE TABLE public."Restaurant" (
    "Id" integer NOT NULL,
    "Name" character varying NOT NULL
);
     DROP TABLE public."Restaurant";
       public         heap    postgres    false    3            �            1259    27391    Restaurant_Id_seq    SEQUENCE     �   CREATE SEQUENCE public."Restaurant_Id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public."Restaurant_Id_seq";
       public          postgres    false    3    210            "           0    0    Restaurant_Id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public."Restaurant_Id_seq" OWNED BY public."Restaurant"."Id";
          public          postgres    false    209            q           2604    27420    Menu Id    DEFAULT     h   ALTER TABLE ONLY public."Menu" ALTER COLUMN "Id" SET DEFAULT nextval('public."Menu_Id_seq"'::regclass);
 :   ALTER TABLE public."Menu" ALTER COLUMN "Id" DROP DEFAULT;
       public          postgres    false    214    213    214            r           2604    27432    MenuGroup Id    DEFAULT     r   ALTER TABLE ONLY public."MenuGroup" ALTER COLUMN "Id" SET DEFAULT nextval('public."MenuGroup_Id_seq"'::regclass);
 ?   ALTER TABLE public."MenuGroup" ALTER COLUMN "Id" DROP DEFAULT;
       public          postgres    false    215    216    216            p           2604    27404    MenuItem Id    DEFAULT     p   ALTER TABLE ONLY public."MenuItem" ALTER COLUMN "Id" SET DEFAULT nextval('public."MenuItem_Id_seq"'::regclass);
 >   ALTER TABLE public."MenuItem" ALTER COLUMN "Id" DROP DEFAULT;
       public          postgres    false    211    212    212            o           2604    27395    Restaurant Id    DEFAULT     t   ALTER TABLE ONLY public."Restaurant" ALTER COLUMN "Id" SET DEFAULT nextval('public."Restaurant_Id_seq"'::regclass);
 @   ALTER TABLE public."Restaurant" ALTER COLUMN "Id" DROP DEFAULT;
       public          postgres    false    210    209    210                      0    27417    Menu 
   TABLE DATA           C   COPY public."Menu" ("Id", "RestaurantId", "CreatedAt") FROM stdin;
    public          postgres    false    214   �0                 0    27429 	   MenuGroup 
   TABLE DATA           J   COPY public."MenuGroup" ("Id", "Name", "SortOrder", "MenuId") FROM stdin;
    public          postgres    false    216   1                 0    27442    MenuGroupItemMap 
   TABLE DATA           I   COPY public."MenuGroupItemMap" ("MenuGroupId", "MenuItemId") FROM stdin;
    public          postgres    false    217   51                 0    27401    MenuItem 
   TABLE DATA           �   COPY public."MenuItem" ("Id", "Name", "Description", "StockStatus", "RestaurantId", "Image", "Ranking", "Price", "Calorie", "IsDeleted") FROM stdin;
    public          postgres    false    212   R1                 0    27392 
   Restaurant 
   TABLE DATA           4   COPY public."Restaurant" ("Id", "Name") FROM stdin;
    public          postgres    false    210   o1       #           0    0    MenuGroup_Id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public."MenuGroup_Id_seq"', 1, false);
          public          postgres    false    215            $           0    0    MenuItem_Id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public."MenuItem_Id_seq"', 1, false);
          public          postgres    false    211            %           0    0    Menu_Id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public."Menu_Id_seq"', 1, true);
          public          postgres    false    213            &           0    0    Restaurant_Id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public."Restaurant_Id_seq"', 1, true);
          public          postgres    false    209            ~           2606    27446 &   MenuGroupItemMap MenuGroupItemMap_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public."MenuGroupItemMap"
    ADD CONSTRAINT "MenuGroupItemMap_pkey" PRIMARY KEY ("MenuGroupId", "MenuItemId");
 T   ALTER TABLE ONLY public."MenuGroupItemMap" DROP CONSTRAINT "MenuGroupItemMap_pkey";
       public            postgres    false    217    217            |           2606    27436    MenuGroup MenuGroup_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public."MenuGroup"
    ADD CONSTRAINT "MenuGroup_pkey" PRIMARY KEY ("Id");
 F   ALTER TABLE ONLY public."MenuGroup" DROP CONSTRAINT "MenuGroup_pkey";
       public            postgres    false    216            v           2606    27410    MenuItem MenuItem_Name_key 
   CONSTRAINT     [   ALTER TABLE ONLY public."MenuItem"
    ADD CONSTRAINT "MenuItem_Name_key" UNIQUE ("Name");
 H   ALTER TABLE ONLY public."MenuItem" DROP CONSTRAINT "MenuItem_Name_key";
       public            postgres    false    212            x           2606    27408    MenuItem MenuItem_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public."MenuItem"
    ADD CONSTRAINT "MenuItem_pkey" PRIMARY KEY ("Id");
 D   ALTER TABLE ONLY public."MenuItem" DROP CONSTRAINT "MenuItem_pkey";
       public            postgres    false    212            z           2606    27422    Menu Menu_pkey 
   CONSTRAINT     R   ALTER TABLE ONLY public."Menu"
    ADD CONSTRAINT "Menu_pkey" PRIMARY KEY ("Id");
 <   ALTER TABLE ONLY public."Menu" DROP CONSTRAINT "Menu_pkey";
       public            postgres    false    214            t           2606    27399    Restaurant Restaurant_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public."Restaurant"
    ADD CONSTRAINT "Restaurant_pkey" PRIMARY KEY ("Id");
 H   ALTER TABLE ONLY public."Restaurant" DROP CONSTRAINT "Restaurant_pkey";
       public            postgres    false    210            �           2606    27447 2   MenuGroupItemMap MenuGroupItemMap_MenuGroupId_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."MenuGroupItemMap"
    ADD CONSTRAINT "MenuGroupItemMap_MenuGroupId_fkey" FOREIGN KEY ("MenuGroupId") REFERENCES public."MenuGroup"("Id");
 `   ALTER TABLE ONLY public."MenuGroupItemMap" DROP CONSTRAINT "MenuGroupItemMap_MenuGroupId_fkey";
       public          postgres    false    217    3196    216            �           2606    27452 1   MenuGroupItemMap MenuGroupItemMap_MenuItemId_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."MenuGroupItemMap"
    ADD CONSTRAINT "MenuGroupItemMap_MenuItemId_fkey" FOREIGN KEY ("MenuItemId") REFERENCES public."MenuItem"("Id");
 _   ALTER TABLE ONLY public."MenuGroupItemMap" DROP CONSTRAINT "MenuGroupItemMap_MenuItemId_fkey";
       public          postgres    false    212    217    3192            �           2606    27437    MenuGroup MenuGroup_MenuId_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."MenuGroup"
    ADD CONSTRAINT "MenuGroup_MenuId_fkey" FOREIGN KEY ("MenuId") REFERENCES public."Menu"("Id");
 M   ALTER TABLE ONLY public."MenuGroup" DROP CONSTRAINT "MenuGroup_MenuId_fkey";
       public          postgres    false    3194    216    214                       2606    27411 #   MenuItem MenuItem_RestaurantId_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."MenuItem"
    ADD CONSTRAINT "MenuItem_RestaurantId_fkey" FOREIGN KEY ("RestaurantId") REFERENCES public."Restaurant"("Id");
 Q   ALTER TABLE ONLY public."MenuItem" DROP CONSTRAINT "MenuItem_RestaurantId_fkey";
       public          postgres    false    212    210    3188            �           2606    27423    Menu Menu_RestaurantId_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public."Menu"
    ADD CONSTRAINT "Menu_RestaurantId_fkey" FOREIGN KEY ("RestaurantId") REFERENCES public."Restaurant"("Id");
 I   ALTER TABLE ONLY public."Menu" DROP CONSTRAINT "Menu_RestaurantId_fkey";
       public          postgres    false    3188    210    214                  x������ � �            x������ � �            x������ � �            x������ � �            x������ � �     